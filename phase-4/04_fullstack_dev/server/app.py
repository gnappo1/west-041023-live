#!/usr/bin/env python3

from flask import (
    Flask,
    request,
    g,
    jsonify,
    abort,
    session,
    make_response
)
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import (
    HTTPException,
    BadRequest,
    UnprocessableEntity,
    InternalServerError,
)
from schemas import ma
from schemas.user_schema import user_schema
from models import db
from models.user import bcrypt, User
from flask_dotenv import DotEnv
from flask_bcrypt import Bcrypt
import os
from datetime import timedelta
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
def create_app():
    from models.crew_member import CrewMember
    from models.production import Production


    from blueprints.productions import Productions
    from blueprints.production_by_id import ProductionByID, production_schema
    from blueprints.crew_members import CrewMembers
    from blueprints.crew_member_by_id import CrewMemberByID, crew_member_schema

    #* Instantiate your flask app
    app = Flask(__name__)
    #* DotEnv wrapper
    env = DotEnv(app)
    #* Configuration settings
    #* Where is the db? /// -> relative path | //// -> absolute path
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater.db"
    #* disabling the modification tracking feature can lead to improved performance and reduced memory usage
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #* Show SQL Queries -> Look at them, how many times do you go into the db per request??
    # app.config["SQLALCHEMY_ECHO"] = True
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    
    # print(app.secret_key)
    #* Flask-Migrate wrapper
    migrate = Migrate(app, db)
    #* Flask-Marshmallow
    #* Flask-RESTful
    api = Api(app, prefix='/api/v1')
    #! Register blueprints
    api.add_resource(Productions, "/productions")
    api.add_resource(ProductionByID, "/productions/<int:id>")
    api.add_resource(CrewMembers, "/crew-members")
    api.add_resource(CrewMemberByID, "/crew-members/<int:id>")

    models_map = {
        'productionbyid': (Production, production_schema),
        'crewmemberbyid': (CrewMember, crew_member_schema)
    }
    def register_error_handlers():
        @app.errorhandler(BadRequest)  # 400
        def handle_bad_request(error):
            response = jsonify({"message": "Bad Request"})
            response.status_code = error.code
            return response

        @app.errorhandler(UnprocessableEntity)  # 422
        def handle_unprocessable_entity(error):
            response = jsonify({"message": "Unprocessable Entity, something looked fishy!"})
            response.status_code = error.code
            return response

        @app.errorhandler(InternalServerError)  # 500
        def handle_internal_server_error(error):
            response = jsonify({"message": "Internal Server Error"})
            response.status_code = error.code
            return response

        @app.errorhandler(HTTPException)  # for any other errors
        def handle_http_exception(error):
            response = jsonify({"message": error.description})
            response.status_code = error.code
            return response

    def register_before_request():
        @app.before_request
        def find_by_id():
            if request.endpoint in ['productionbyid', 'crewmemberbyid']:
                id_ = request.view_args.get('id')
                class_ = models_map.get(request.endpoint)[0]
                schema = models_map.get(request.endpoint)[1]
                if data := class_.query.get(id_):
                    g.data = data
                else:
                    abort(404, f"Could not find {str(class_)} with id {id_}")

    def register_routes():
        @app.route("/")
        def welcome():
            #! You can use a template for the landing page of your api-only flask app
            #! or you can just return a string
            #* This landing page is not of great importance, but it's nice to have one
            #* The real one will live inside the client folder
            return """
                <h1>Welcome to our Theater!</h1>
                <figure>
                    <img style="width: 80vw; height: 70vh;" src="https://images.unsplash.com/photo-1503095396549-807759245b35?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=kyle-head-p6rNTdAPbuk-unsplash.jpg" alt="Theater">
                    <figcaption>
                        <span class="caption">A theater red backdrop, with the shadows of three actors in front of it.</span>
                        <i class="photo-credit">Photo by <a href="https://unsplash.com/it/@kyleunderscorehead?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kyle Head</a> on <a href="https://unsplash.com/photos/p6rNTdAPbuk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></i>
                    </figcaption>
                </figure>
                <p>Check out our <a href="/api/v1/productions">productions</a> and <a href="/api/v1/crew-members">crew members</a>!</p>
            """

        @app.route("/login", methods=["POST"])
        def login():
            user_info = request.get_json()
            
    # Register error handlers, before request function, and routes
    register_error_handlers()
    register_before_request()
    register_routes()
    return app, models_map

app, models_map = create_app()
#* Flask-SQLAlchemy wrapper
db.init_app(app)
#* Flask-Marshmallow
ma.init_app(app)
#* Flask-Bcrypt
bcrypt.init_app(app)
#* Flask-JWT-Extended
jwt = JWTManager(app)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=2)
#! Authentication starts here

@app.route("/api/v1/signup", methods=["POST"])
def signup():
    user_info = request.get_json()
    try:
        user = user_schema.load({"username": user_info.get('username', ""), "email": user_info.get('email', "")})
        user.password_hash = user_info.get("password", "")
        db.session.add(user)
        db.session.commit()
        # session["user_id"] = user.id
        token = create_access_token(identity=user.id)
        refresh_token = create_access_token(identity=user.id)
        return make_response({"user": user_schema.dump(user), 'token': token, 'refresh_token': refresh_token}, 201)
    except Exception as e:
        return make_response({"error": str(e)}, 400)
    
@app.route("/api/v1/signin", methods=["POST"])
def signin():
    user_info = request.get_json()
    if user := User.query.filter_by(email=user_info.get("email", "")).first():
        if user.authenticate(user_info.get("password_hash", "")):
            # session["user_id"] = user.id
            token = create_access_token(identity=user.id)
            refresh_token = create_access_token(identity=user.id)
            return make_response({"user": user_schema.dump(user), 'token': token, 'refresh_token': refresh_token}, 200)
    return make_response({"error": "Invalid credentials"}, 401)


@app.route("/api/v1/logout", methods=["DELETE"])
def logout():
    # session.pop("user_id", None)
    return make_response({}, 204)

@app.route("/api/v1/me", methods=["GET"])
@jwt_required()
def me():
    # if id_ := get_jwt_identity(): #session.get("user_id", None):
    if user := User.query.get(get_jwt_identity()):
        return make_response(user_schema.dump(user), 200)
    return make_response({"error": "Unauthorized"}, 401)

@app.route("/api/v1/refresh_token", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    id_ = get_jwt_identity()
    try:
        user = User.query.get(id_)
    
        token = create_access_token(identity=user.id)
        # refresh_token = create_access_token(identity=user.id)
        return make_response({"user": user_schema.dump(user), 'token': token}, 200)
    except Exception as e:
        return make_response({"error": "User not found"}, 404)
if __name__ == "__main__":
    app.run(debug=True, port=5555)

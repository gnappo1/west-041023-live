#!/usr/bin/env python3

# 📚 Review With Students:
    # API Fundamentals
    # MVC Architecture and Patterns / Best Practices
    # RESTful Routing
    # Serialization
    # Postman

# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5000
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py

# Restful

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all resources 	|
# | GET       	| /productions/:id 	| READ one resource   	|
# | POST      	|   /productions   	| CREATE one resource 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
# | DELETE    	| /productions/:id 	| DESTROY one resource 	|



from flask import (
    Flask,
    request,
    g,
    session,
    json,
    jsonify,
    render_template,
    make_response,
    url_for,
    redirect,
    abort
)
from werkzeug.exceptions import HTTPException, BadRequest, UnprocessableEntity, InternalServerError
from flask_migrate import Migrate
from models import db, Production, CrewMember
from time import time
# 1. ✅ Import `Api` and `Resource` from `flask_restful`
    # ❓ What do these two classes do at a higher level?
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title field is required.')
parser.add_argument('genre', type=str, required=True, help='Genre field is required.')
parser.add_argument('director', type=str, required=True, help='Director field is required.')
parser.add_argument('description', type=str, required=True, help='Description field is required.')
parser.add_argument('budget', type=float, required=True, help='Budget field is required.')
parser.add_argument('image', type=str, required=True, help='Image field is required.')
parser.add_argument('ongoing', type=bool, required=True, help='Ongoing field is required.')

# Error handling for 400 Bad Request
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify({'message': 'Bad Request'})
    response.status_code = error.code
    return response

# Error handling for 422 Unprocessable Entity
@app.errorhandler(UnprocessableEntity)
def handle_unprocessable_entity(error):
    response = jsonify({'message': 'Unprocessable Entity'})
    response.status_code = error.code
    return response

# Error handling for 500 Internal Server Error
@app.errorhandler(InternalServerError)
def handle_internal_server_error(error):
    response = jsonify({'message': 'Internal Server Error'})
    response.status_code = error.code
    return response

# Error handling for all other HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    response = jsonify({'message': error.description})
    response.status_code = error.code
    return response

@app.route("/")
def welcome():
    return "<h1>Welcome to our Theater!</h1>"

# 3. ✅ Create a Production class that inherits from Resource

# 4. ✅ Create a GET (All) Route

class Productions(Resource):
    def get(self):
        #check out self and explore attributes/properties like: methods, endpoint, ...
        productions = [p.to_dict() for p in Production.query.all()]
        return make_response(productions, 200)
        
    def post(self):
        # inspect the request object
        # useful methods 'args', 'headers', 'cookies', 'data', get_json(), get_data(), json(), 'method', 'mimetype','path', 'url',
        
        args = parser.parse_args()
        # Access the parsed and validated data
        title = args['title']
        genre = args['genre']
        director = args['director']
        description = args['description']
        budget = args['budget']
        image = args['image']
        ongoing = args['ongoing']
        
        # Perform validations
        self.validate_title(title)
        self.validate_description(description)
        
        import ipdb; ipdb.set_trace()
        try:
            prod = Production(title=title, genre=genre, director=director, budget=budget, image=image, ongoing=ongoing, description=description)
            db.session.add(prod)
            db.session.commit()
            return prod.as_dict(), 201
        
        except Exception as e:
            db.session.rollback()
            abort(422, "You somehow bypassed by most immediate defenses")
            
    def validate_title(self, title):
        if len(title) > 3:
            raise BadRequest('title must be at least 3 characters long.')

    def validate_description(self, description):
        if len(description) > 100:
            raise BadRequest('Description must be at least 100 characters long.')
        
api.add_resource(Productions, '/productions')

class ProductionByID(Resource):
    def get(self, id):
        prod = db.session.get(Production, id)
        
        if not prod:
            abort(404, "The Production you are looking for does not exist!")
        
        return make_response(prod.as_dict(), 200)

api.add_resource(ProductionByID, "/productions/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=5555)
#!/usr/bin/env python3

# 📚 Review With Students:
# API Fundamentals
# MVC Architecture and Patterns / Best Practices
# RESTful Routing
# Serialization
# Postman

# Set Up When starting from scratch:
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
    abort,
)

from flask_migrate import Migrate
from models import db, Production, CrewMember
from time import time
from flask_restful import Api, Resource, reqparse
from werkzeug.exceptions import (
    HTTPException,
    BadRequest,
    UnprocessableEntity,
    InternalServerError,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("title", type=str, required=True, help="Title must be present")
parser.add_argument("genre", type=str, required=True, help="genre must be present")
parser.add_argument(
    "description", type=str, required=True, help="description must be present"
)
parser.add_argument(
    "director", type=str, required=True, help="director must be present"
)
parser.add_argument("budget", type=float, required=True, help="budget must be present")
parser.add_argument("image", type=str, required=True, help="image must be present")
parser.add_argument("ongoing", type=bool, required=True, help="ongoing must be present")


@app.errorhandler(BadRequest)  # 400
def handle_bad_request(error):
    response = jsonify({"message": "Bad Request"})
    response.status_code = error.code
    return response


@app.errorhandler(UnprocessableEntity)  # 422
def handle_bad_request(error):
    response = jsonify({"message": "Unprocessible Entity, something looked fishy!"})
    response.status_code = error.code
    return response


@app.errorhandler(InternalServerError)  # 500
def handle_bad_request(error):
    response = jsonify({"message": "Internal Server Error"})
    response.status_code = error.code
    return response


@app.errorhandler(HTTPException)  # for any other errors
def handle_bad_request(error):
    response = jsonify({"message": error.description})
    response.status_code = error.code
    return response


@app.route("/")
def welcome():
    return "<h1>Welcome to our Theater!</h1>"


class Productions(Resource):
    def get(self):
        # check out self and explore attributes/properties like: methods, endpoint, ...
        prods = [prod.to_dict() for prod in Production.query.all()]
        return make_response(prods, 200)

    def post(self):
        # inspect the request object
        # useful methods 'args', 'headers', 'cookies', 'data', get_json(), get_data(), json(), 'method', 'mimetype','path', 'url',
        # data = request.get_json()
        data = parser.parse_args()
        # perform extra validations!!!
        self.validate_title(data["title"])

        try:
            prod = Production(**data)
            db.session.add(prod)
            db.session.commit()
            return make_response(prod.to_dict(), 201)
        except:
            db.session.rollback()
            abort(400, "There was a problem with the values provided!")

    def validate_title(self, title):
        if len(title) < 3:
            raise BadRequest("title must be longer than 3 characters!!!")


api.add_resource(Productions, "/productions")


class ProductionByID(Resource):
    def get(self, id):
        if prod := Production.query.get(id):
            # return make_response(prod, 200)
            return make_response(prod.to_dict(), 200)
        else:
            abort(404, f"Could not find Production with id {id}")


api.add_resource(ProductionByID, "/productions/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=5555)

#!/usr/bin/env python3

from flask import (
    Flask,
    request,
    g,
    jsonify,
    make_response,
    abort,
)
from flask_migrate import Migrate
from models import db, Production, CrewMember
from flask_restful import Api, Resource, reqparse
from flask_marshmallow import Marshmallow
from marshmallow import fields, validates, validate, ValidationError
from werkzeug.exceptions import (
    HTTPException,
    BadRequest,
    UnprocessableEntity,
    InternalServerError,
)
from sqlalchemy.exc import SQLAlchemyError
#* Instantiate your flask app
app = Flask(__name__)
#* Configuration settings
#* Where is the db? /// -> relative path | //// -> absolute path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater.db"
#* disabling the modification tracking feature can lead to improved performance and reduced memory usage
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#* Show SQL Queries -> Look at them, how many times do you go into the db per request??
app.config["SQLALCHEMY_ECHO"] = True

#* Flask-Migrate wrapper
migrate = Migrate(app, db)
#* Flask-SQLAlchemy wrapper
db.init_app(app)
#* Flask-Marshmallow
ma = Marshmallow(app)
#* Flask-RESTful
api = Api(app)

#* Example of using reqparse for app-level validations
#* And encapsulated the code into a Mixin to extend other classes functionality
class ParserMixin:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str, required=True, help="Title must be present")
        self.parser.add_argument("genre", type=str, required=True, help="genre must be present")
        self.parser.add_argument(
            "description", type=str, required=True, help="description must be present"
        )
        self.parser.add_argument(
            "director", type=str, required=True, help="director must be present"
        )
        self.parser.add_argument("budget", type=float, required=True, help="budget must be present")
        self.parser.add_argument("image", type=str, required=True, help="image must be present")
        self.parser.add_argument("ongoing", type=bool, required=True, help="ongoing must be present")

class CrewMemberSchema(ma.SQLAlchemySchema):
    class Meta():
        # name of model
        model = CrewMember
        # avoid recreating objects on updates, only applies to deserialization (load())
        # in order for this to work, flask-marshmallow (is specific to this wrapper)
        # needs to know how an instance even looks like, note how we invoked load() on line 222
        load_instance = True
        #  if you set to True, Marshmallow will preserve the order of fields as defined in the schema.
        ordered = True
        # Specify which fields to serialize (not deserialize)
        fields = ('id', 'name', 'role', 'production_id', 'production', 'url')
    
    #! Setup some app-level (aka no DB involved) validations
    #* See more here https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#module-marshmallow.validate
    name = fields.String(required=True)
    production = fields.Nested('ProductionSchema', exclude=('crew_members', ))
    role = fields.String(required=True, validate=validate.Length(min=3, max=50, error="Role should be a string at least 3 chars long! But max 50!"))
    
    #! Create hyperlinks for easy navigation of your api
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                'crewmemberbyid',
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor('crewmembers')
        }
    )
    
    #! Example of custom validation with marshmallow 
    #! (DANGER -> VERY similar to the syntax in the models)
    @validates('name')
    def validate_word_count(self, name):
        words = name.split()
        if len(words) < 2:
            raise ValidationError('Text must contain at least two words')

#! Create schema for a single crew_member
crew_member_schema = CrewMemberSchema()
#! Create schema for a collection of crew_members
#* Feel free to use only and exclude to customize
crew_members_schema = CrewMemberSchema(many=True)

class ProductionSchema(ma.SQLAlchemySchema):
    #! The notes are the same as above in CrewMemberSchema ^^^
    class Meta():
        model = Production
        load_instance = True
        fields = ('title', 'genre', 'budget', 'director', 'description', 'id', 'image', 'ongoing', 'crew_members', 'url')

    crew_members = fields.Nested(CrewMemberSchema, only=('id', 'name', 'role'), exclude=('production',), many=True)
    title = fields.String(required=True, validate=validate.Length(min=2, max=50))
    director = fields.String(required=True, validate=validate.Length(min=2, max=50))
    description = fields.String(required=True, validate=validate.Length(min=30, max=500))
    genre = fields.String(required=True, validate=validate.Length(min=2, max=50))
    image = fields.String(required=True, validate=validate.Regexp(r'.*\.(jpeg|png)', error="File URI must be in JPEG or PNG format"))
    budget = fields.Float(required=True, validate=validate.Range(min=0.99, max=500000000))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "productionbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("productions"),
            "crewmembers": ma.URLFor(
                "crewmembers"
            )
        }
    )
    
#! Create schema for a single crew_member
production_schema = ProductionSchema()
#! Create schema for a collection of crew_members
#* Feel free to use only and exclude to customize
productions_schema = ProductionSchema(many=True, exclude=('crew_members', ))

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

models_map = {
    'productionbyid': (Production, production_schema),
    'crewmemberbyid': (CrewMember, crew_member_schema)
}

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

@app.route("/")
def welcome():
    return "<h1>Welcome to our Theater!</h1>"

class Productions(Resource):
    def get(self):
        prods = productions_schema.dump(Production.query.all())
        return make_response(prods, 200)

    def post(self):
        try:
            #* Extract data out of the request
            data = request.json
            with db.session.begin():
                #* Validate the data, if problems arise you'll see ValidationError
                production_schema.validate(data)
                #* Deserialize the data with dump()
                prod = production_schema.load(data)
                db.session.add(prod)
        
            #* Serialize the data and package your JSON response
            serialized_product = production_schema.dump(prod)
            return make_response(serialized_product, 201)
        except (ValidationError, ValueError) as e:
            db.session.rollback()
            abort(400, str(e))

api.add_resource(Productions, "/productions")

class ProductionByID(Resource):

    def get(self, id):
        serialized_data = production_schema.dump(g.get('data'))
        return make_response(serialized_data, 200)
            
    def patch(self, id):
        try:
            #* The before_action stored inside g under a key called 'data' the production
            production = g.get('data')
            #* get the data out of the request
            data = request.json
            
            # with db.session.begin():            
            #* Validate the data, if problems arise you'll see ValidationError
            production_schema.validate(data)
            #* partial = True allows partial updates, meaning only the provided fields 
            #* in the JSON data will be updated, and the rest will remain unchanged.
            #* Remember what we said about passing the instance to load() in order
            #* for marshmallow to reuse an existing object rather than recreating one?
            updated_prod = production_schema.load(data, instance=production, partial=True)
            db.session.commit()
            #* Now serialize the object and package JSON data
            serialized_prod = production_schema.dump(updated_prod)
            return make_response(serialized_prod, 200)
        #! ma error that will be raised in case the schema validations are not met 
        except ValidationError as e:
            abort(400, str(e))
        #! sqlalchemy.orm error that will be raised by @validates in the model
        except ValueError as e:
            abort(400, str(e))

    def delete(self, id):
        try:
            # prod = production_schema.dump(g.get('data'))
            db.session.delete(g.get('data'))
            db.session.commit()
            return make_response("", 204)
        except ValueError as e:
            abort(400, str(e))

api.add_resource(ProductionByID, "/productions/<int:id>")

class CrewMembers(Resource):
    def get(self):
        crew = crew_members_schema.dump(CrewMember.query.all())
        return make_response(crew, 200)
    
    def post(self):
        try:
            data = request.json
            with db.session.begin():
                #* Validate the data, if problems arise you'll see ValidationError
                crew_member_schema.validate(data)
                #* Deserialize the data with dump()
                crew = crew_member_schema.load(data)
                db.session.add(crew)
        
            #* Serialize the data and package your JSON response
            serialized_crew = crew_member_schema.dump(crew)
            return make_response(serialized_crew, 201)
        except (ValidationError, ValueError) as e:
            abort(400, str(e))
                
api.add_resource(CrewMembers, "/crewmembers")

class CrewMemberByID(Resource):
    def get(self, id):
        serialized_data = crew_member_schema.dump(g.get('data'))
        return make_response(serialized_data, 200)
        
    def patch(self, id):
        try:
            crew = g.get('data')
            data = request.json
            crew_member_schema.validate(data)
            updated_crew = crew_member_schema.load(data, instance=crew, partial=True)
            db.session.commit()
            
            serialized_crew = crew_member_schema.dump(updated_crew)
            return make_response(serialized_crew, 200)
        #! ma error that will be raised in case the schema validations are not met 
        except ValidationError as e:
            abort(400, str(e))
        #! sqlalchemy.orm error that will be raised by @validates in the model
        except ValueError as e:
            abort(400, str(e))
                

    def delete(self, id):
        try:
            # prod = production_schema.dump(g.get('data'))
            db.session.delete(g.get('data'))
            db.session.commit()
            return make_response("", 204)
        except ValueError as e:
            abort(400, str(e))

api.add_resource(CrewMemberByID, "/crewmembers/<int:id>")
if __name__ == "__main__":
    app.run(debug=True, port=5555)

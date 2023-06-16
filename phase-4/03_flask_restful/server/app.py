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

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

migrate = Migrate(app, db)
db.init_app(app)

ma = Marshmallow(app)
api = Api(app)
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
        model = CrewMember # name of model
        load_instance = True
        ordered = True
        fields = ('id', 'name', 'role', 'production_id', 'production', 'url')
    
    name = fields.String(required=True)
    production = fields.Nested('ProductionSchema', exclude=('crew_members', ))
    role = fields.String(required=True, validate=validate.Length(min=3, max=50, error="Role should be a string at least 3 chars long! But max 50!"))
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                'crewmemberbyid',
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor('crewmembers')
        }
    )
    
    @validates('name')
    def custom_validation(self, data):
        if type(data) is not str or len(data) < 3:
            raise ValidationError('Name has to be a string at least 3 chars long')

crew_member_schema = CrewMemberSchema()
crew_members_schema = CrewMemberSchema(many=True)

class ProductionSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Production # name of model
        load_instance = True
        ordered = True
        fields = ('id', 'title', 'genre', 'budget', 'description', 'director', 'image', 'ongoing', 'crew_members', 'url')

    title = fields.String(required=True)
    genre = fields.String(required=True)
    crew_members = fields.Nested(CrewMemberSchema, only=('id', 'role'), exclude=('production',), many=True)
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                'productionbyid',
                values=dict(id="<id>")
            ),
            "collection": ma.URLFor('productions'),
            "crewmembers": ma.URLFor('crewmembers')
        }
    )
production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True, exclude=('crew_members', ))

# @app.errorhandler(BadRequest)  # 400
# def handle_bad_request(error):
#     response = jsonify({"message": "Bad Request"})
#     response.status_code = error.code
#     return response


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


# @app.errorhandler(HTTPException)  # for any other errors
# def handle_bad_request(error):
#     response = jsonify({"message": error.description})
#     response.status_code = error.code
#     return response

@app.before_request
def find_prod_by_id():
    if request.endpoint == 'productionbyid':
        id_ = request.view_args.get('id')
        if prod := Production.query.get(id_):
            g.prod = production_schema.dump(prod)
        else:
            abort(404, f"Could not find Production with id {id_}")

def format_ma_errors(e):
    errors = "".join(f"{attr.title()}: {e.get(attr)[0].lower()}" for attr in e)
    abort(424, errors)

@app.route("/")
def welcome():
    return "<h1>Welcome to our Theater!</h1>"

class Productions(Resource):
    def get(self):
        # check out self and explore attributes/properties like: methods, endpoint, ...
        prods = productions_schema.dump(Production.query.all())
        return make_response(prods, 200)

    def post(self):
        try:
            if errors := production_schema.validate(request.get_json()):
                format_ma_errors(errors)
            prod = production_schema.load(request.get_json())
            db.session.add(prod)
            db.session.commit()
            serialized_product = production_schema.dump(prod)
            return make_response(serialized_product, 201)
        except Exception as e:
            db.session.rollback()
            abort(400, str(e))

api.add_resource(Productions, "/productions")


class ProductionByID(Resource):

    def get(self, id):
        return make_response(g.get('prod'), 200) if g.get('prod') else abort(404, "DO we even get here???")
            
    def patch(self, id):
        try:
            prod = g.get('prod')
            data = request.get_json()
            for attr in data:
                setattr(prod, attr, data.get(attr))
            db.session.add(prod)
            db.session.commit()
            return make_response(prod.to_dict(), 200)
        except Exception as e:
            import ipdb; ipdb.set_trace()
            abort(404, e)

    def delete(self, id):
        try:
            prod = g.get('prod')
            db.session.delete(prod)
            db.session.commit()
            return make_response("", 204)
        except Exception as e:
            abort(400, "Something went wrong while deleting!")

api.add_resource(ProductionByID, "/productions/<int:id>")


class CrewMembers(Resource):
    def get(self):
        crew = [cm.to_dict() for cm in CrewMember.query.all()]
        return make_response(crew, 200)

    def post(self):
        try:
            data = request.get_json()
            cm = CrewMember(**data)
            db.session.add(cm)
            db.session.commit()
            return make_response(cm.to_dict(), 201)
        except Exception as e:
            abort(422, "Incorrect Data!")
                
api.add_resource(CrewMembers, "/crewmembers")

class CrewMemberByID(Resource):
    def get(self, id):
        if crew:= CrewMember.query.get(id):
            # return make_response(crew, 200)
            return make_response(crew.to_dict(), 200)
        else:
            abort(404, f"Could not find CrewMember with id {id}")

api.add_resource(CrewMemberByID, "/crewmembers/<int:id>")
if __name__ == "__main__":
    app.run(debug=True, port=5555)

from models.production import Production
from models import db

from blueprints import abort, make_response, request, Resource, Blueprint, ValidationError
from blueprints.production_by_id import production_schema, ProductionSchema

productions_schema = ProductionSchema(many=True, exclude=("crew_members",))
productions_bp = Blueprint('productions', __name__, url_prefix='/productions')

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

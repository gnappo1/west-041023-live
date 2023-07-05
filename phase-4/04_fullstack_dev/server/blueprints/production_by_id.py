from blueprints import (
    request,
    Blueprint,
    make_response,
    g,
    abort,
    ValidationError,
    Resource,
    login_required,
)
from models import db
from schemas.production_schema import ProductionSchema

production_schema = ProductionSchema()
production_by_id_bp = Blueprint(
    "production_by_id", __name__, url_prefix="/productions/<int:id>"
)


class ProductionByID(Resource):
    def get(self, id):
        serialized_data = production_schema.dump(g.get("data"))
        return make_response(serialized_data, 200)

    @login_required
    def patch(self, id):
        try:
            # * The before_action stored inside g under a key called 'data' the production
            production = g.get("data")
            # * get the data out of the request
            data = request.json

            # with db.session.begin():
            # * Validate the data, if problems arise you'll see ValidationError
            production_schema.validate(data)
            # * partial = True allows partial updates, meaning only the provided fields
            # * in the JSON data will be updated, and the rest will remain unchanged.
            # * Remember what we said about passing the instance to load() in order
            # * for marshmallow to reuse an existing object rather than recreating one?
            updated_prod = production_schema.load(
                data, instance=production, partial=True
            )
            db.session.commit()
            # * Now serialize the object and package JSON data
            serialized_prod = production_schema.dump(updated_prod)
            return make_response(serialized_prod, 200)
        #! ma error that will be raised in case the schema validations are not met
        except (ValidationError, ValueError) as e:
            abort(400, str(e))

    @login_required
    def delete(self, id):
        try:
            db.session.delete(g.get("data"))
            db.session.commit()
            return make_response("", 204)
        except ValueError as e:
            abort(400, str(e))

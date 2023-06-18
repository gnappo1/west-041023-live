from models.crew_member import CrewMember
from models import db

from blueprints import request, Blueprint, make_response, abort, ValidationError, Resource
from blueprints.crew_member_by_id import crew_member_schema, CrewMemberSchema

crew_members_schema = CrewMemberSchema(many=True, exclude=("production",))
crew_members_bp = Blueprint('crew_members', __name__, url_prefix='/crew-members')

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

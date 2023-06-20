from schemas import fields, validate, ma, Production
from schemas.crew_member_schema import CrewMemberSchema
class ProductionSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Production
        load_instance = True
        fields = ('title', 'genre', 'budget', 'director', 'description', 'id', 'image', 'ongoing', 'crew_members', 'url')

    crew_members = fields.Nested(CrewMemberSchema, only=('id', 'name', 'role'), exclude=('production',), many=True)
    title = fields.String(required=True, validate=validate.Length(min=2, max=50))
    director = fields.String(required=True, validate=validate.Length(min=2, max=50))
    description = fields.String(required=True, validate=validate.Length(min=30, max=500))
    genre = fields.String(required=True, validate=validate.Length(min=2, max=50))
    image = fields.String(required=True, validate=validate.Regexp(r'.*\.(jpeg|jpg|png)', error="File URI must be in JPEG, JPG or PNG format"))
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

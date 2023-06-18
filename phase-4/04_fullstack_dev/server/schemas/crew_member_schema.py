from schemas import fields, validate, validates, ValidationError, ma, CrewMember
class CrewMemberSchema(ma.SQLAlchemySchema):
    class Meta():
        model = CrewMember
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
    
    #! Example of custom validation with marshmallow 
    #! (DANGER -> VERY similar to the syntax in the models)
    @validates('name')
    def validate_word_count(self, name):
        words = name.split()
        if len(words) < 2:
            raise ValidationError('Text must contain at least two words')

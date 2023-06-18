from schemas.__init__ import ma, fields, validate, validates, ValidationError, CrewMember
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

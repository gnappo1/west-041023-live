from schemas import fields, validate, ma, validates, ValidationError
from models.user import User
import re

class UserSchema(ma.SQLAlchemySchema):
    class Meta():
        model = User
        load_instance = True
        fields = ('username', 'id', 'email')

    username = fields.String(required=True, validate=validate.Length(min=8, max=20))
    email = fields.String(required=True)
    
    
    @validates('email')
    def validate_email(self, email):
        if type(email) is not str or not re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|'(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*')@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", email):
            raise ValueError(f'{email} does not match the email format')
        
        if User.query.filter(User.email == email).first():
            raise ValueError(f'{email} is already taken')
        
        
user_schema = UserSchema()
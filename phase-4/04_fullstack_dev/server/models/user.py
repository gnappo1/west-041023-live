from models import db, validates, re
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed")
    
    @password_hash.setter
    def password_hash(self, password):
        self.validate_password(password)
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return (
            f"<User #{self.id}:\n"
            + f"Username: {self.username}\n"
            + f"Email: {self.email}"
        )

    @validates('username')
    def validate_username(self, key, username):
        if type(username) is not str or len(username) < 8:
            raise ValueError(f'{username} has to be at least 3 characters long')
        if User.query.filter(User.username == username).first():
            raise ValueError(f'{username} is already taken')
        return username

    @validates('email')
    def validate_email(self, key, email):
        if type(email) is not str or not re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|'(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*')@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", email):
            raise ValueError(f'{email} does not match the email format')
        return email
        
    def validate_password(self, password):
        if type(password) is not str or len(password) < 10:
            raise ValueError(f'{password} has to be at least 10 characters long')
        if not re.search(r'[A-Z]', password):
            raise ValueError(f'{password} has to have at least one uppercase letter')
        if not re.search(r'[a-z]', password):
            raise ValueError(f'{password} has to have at least one lowercase letter')
        if not re.search(r'[0-9]', password):
            raise ValueError(f'{password} has to have at least one number')
        if not re.search(r'[^A-Za-z0-9]', password):
            raise ValueError(f'{password} has to have at least one special character')
        return password
        

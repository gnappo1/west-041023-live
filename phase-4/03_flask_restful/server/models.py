from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import re
db = SQLAlchemy()
class Production(db.Model):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False)
    ongoing = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    #&* Relationships
    crew_members = db.relationship(
        "CrewMember", back_populates="production", cascade="all"
    )

    def __repr__(self):
        return (
            f"<Production #{self.id}:\n"
            + f"Title: {self.title}"
            + f"Genre: {self.genre}"
            + f"Director: {self.director}"
            + f"Budget: {self.budget}"
            + f"Image: {self.image}"
            + f"Ongoing: {self.ongoing}"
            + f"Description: {self.description}"
        )

    @validates('title')
    def validate_title(self, key, title):
        if type(title) is not str or len(title) < 3:
            raise ValueError(f'{title} has to be at least 3 characters long')
        return title

    @validates('genre') #presence and inclusion
    def validate_genre(self, key, genre):
        if type(genre) is not str or genre not in ['Drama', 'Musical', 'Opera']:
            raise ValueError(f'{genre} has to be one of Drama, Musical, Opera')
        return genre
    
    @validates('director')
    def validate_director(self, key, director):
        if type(director) is not str or len(director.split(' ')) < 2:
            raise ValueError(f'{director} has to be a string of at least two words')
        return director
    
    @validates('description')
    def validate_description(self, key, description):
        if type(description) is not str or len(description) < 10:
            raise ValueError(f'{description} has to be a string of at least 10 characters')
        return description
    
    @validates('budget')
    def validate_budget(self, key, budget):
        if type(budget) is not float or budget < 0 or budget > 10000000:
            raise ValueError(f'{budget} has to be a positive float under 1Million')
        return budget
    
    @validates('image')
    def validate_image(self, key, image):
        if type(image) is not str or not re.match(r'^https?:\/\/.*\.(?:png|jpeg)$', image):
            raise ValueError(f'{image} has to be a string of a valid url ending in png or jpg')
        return image
    
    @validates('ongoing')
    def validate_ongoing(self, key, ongoing):
        if type(ongoing) is not bool:
            raise ValueError(f'{ongoing} has to be a boolean')
        return ongoing
        
class CrewMember(db.Model):
    __tablename__ = "crew_members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    production_id = db.Column(db.Integer, db.ForeignKey("productions.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    production = db.relationship("Production", back_populates="crew_members")

    def __repr__(self):
        return (
            f"<CrewMember #{self.id}:\n"
            + f"Name: {self.name}"
            + f"Role: {self.role}"
            + f"Production_id: {self.production_id}"
        )
    
    @validates('name')
    def validate_name(self, key, name):
        if type(name) is not str or len(name.split(' ')) < 2:
            raise ValueError(f'{name} has to be at least 2 words')
        return name
    
    @validates('role')
    def validate_role(self, key, role):
        if type(role) is not str or len(role) < 2:
            raise ValueError(f'{role} has to be at least 3 characters long')
        return role
    
    @validates('production_id')
    def validate_production_id(self, key, production_id):
        if not production_id or type(production_id) is not int or production_id < 1 or not Production.query.get(production_id):
            raise ValueError(f'{production_id} has to be a positive integer corresponding to an existing production')
        return production_id

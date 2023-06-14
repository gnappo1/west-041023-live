from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    crew_members = db.relationship('CrewMember', back_populates='production', cascade='all, delete-orphan')
    
    serialize_rules = (
        "-crew_members.production",
    )
    def __repr__(self):
        return f"<Production #{self.id}\n title: {self.title}\n genre: {self.genre}\n director: {self.director}\n description: {self.description}\n budget: {self.budget}\n image: {self.image}\n ongoing: {self.ongoing}>"
    
    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "director": self.director,
            "description": self.description,
            "budget": self.budget,
            "image": self.image,
            "ongoing": self.ongoing,
            "crew_members": [crew_member.as_dict() for crew_member in self.crew_members]
        }

class CrewMember(db.Model, SerializerMixin):
    __tablename__ = "crew_members"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    production = db.relationship('Production', back_populates='crew_members')   
    # serialize_rules = (
    #     "-production.crew_members",
    # )
    def __repr__(self):
        return f"<CrewMember #{self.id}\n name: {self.name}\n role: {self.role}\n production_id: {self.production_id}>"
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "production_id": self.production_id
        }

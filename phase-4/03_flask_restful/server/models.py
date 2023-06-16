from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

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

    @validates('title', 'genre')
    def validate_title(self, key, value):
        if not value or len(value) < 3:
            raise ValueError(f'{key.title()} must be a string of at least 3 characters')

    @validates('director')
    def validate_director(self, _, value):
        if not value or type(value) is not str or len(value.split(" ")) < 2:
            raise ValueError('Director must contain at least 2 words')
        
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
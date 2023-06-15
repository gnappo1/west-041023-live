from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Production(db.Model, SerializerMixin):
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
    crew_members = db.relationship(
        "CrewMember", back_populates="production", cascade="all"
    )

    # serialize_only = ("id", "title", "crew_members") #recursive stack level too deep
    serialize_rules = ("-crew_members.production", "-created_at", "-updated_at")

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

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "director": self.director,
            "budget": self.budget,
            "image": self.image,
            "ongoing": self.ongoing,
            "description": self.description,
        }


class CrewMember(db.Model, SerializerMixin):
    __tablename__ = "crew_members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    production_id = db.Column(db.Integer, db.ForeignKey("productions.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    production = db.relationship("Production", back_populates="crew_members")

    serialize_rules = ("-production.crew_members", "-created_at", "-updated_at")

    def __repr__(self):
        return (
            f"<Production #{self.id}:\n"
            + f"Name: {self.name}"
            + f"Role: {self.role}"
            + f"Production_id: {self.production_id}"
        )

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "production_id": self.production_id,
        }

from models import db, validates
from models.production import Production
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

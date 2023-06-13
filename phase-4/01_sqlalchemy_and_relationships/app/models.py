import re
from datetime import datetime

from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    Float,
    String,
    DateTime,
    Date,
    PrimaryKeyConstraint,
    ForeignKey,
    CheckConstraint,
    func,
    text,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)
Base = declarative_base(metadata=metadata)


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String)
    breed = Column(String)
    temperament = Column(String)
    species = Column(String)
    owner_id = Column(Integer, ForeignKey("owners.id"))
    owner = relationship("Owner", back_populates="pets")
    jobs = relationship("Job", back_populates="pet", cascade="all, delete-orphan")
    handlers = association_proxy(
        "jobs", "handler", creator=lambda handler: Job(handler=handler)
    )

    def __repr__(self):
        return (
            f"<Pet #{self.id} \n"
            + f"name: {self.name}\n"
            + f"species: {self.species}\n"
            + f"breed: {self.breed}\n"
            + f"temperament: {self.temperament}\n"
            + f"owner_id: {self.owner_id}\n"
        )


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(Integer, unique=True)
    address = Column(String)
    pets = relationship("Pet", back_populates="owner", cascade="all, delete-orphan")
    # pets = relationship("Pet", backref=backref('owner'), cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"<Owner #{self.id} \n"
            + f"name: {self.name}\n"
            + f"email: {self.email}\n"
            + f"phone: {self.phone}\n"
            + f"address: {self.address}\n"
        )


# owners -> pets -> jobs <- handlers


class Handler(Base):
    __tablename__ = "handlers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(Integer, unique=True)
    hourly_rate = Column(Float, nullable=False)
    jobs = relationship("Job", back_populates="handler", cascade="all, delete-orphan")
    pets = association_proxy(
        "jobs", "pet", creator=lambda pet: Job(pet=pet)
    )
    
    def __repr__(self):
        return (
            f"<Handler #{self.id} \n"
            + f"name: {self.name}\n"
            + f"email: {self.email}\n"
            + f"phone: {self.phone}\n"
            + f"hourly_rate: {self.hourly_rate}\n"
        )


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    notes = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    request = Column(String, nullable=False)
    fee = Column(Float, nullable=False)
    handler_id = Column(Integer, ForeignKey("handlers.id"))
    pet_id = Column(Integer, ForeignKey("pets.id"))
    pet = relationship("Pet", back_populates="jobs")
    handler = relationship("Handler", back_populates="jobs")

    def __repr__(self):
        return (
            f"<Job #{self.id} \n"
            + f"date: {self.date}\n"
            + f"fee: {self.fee}\n"
            + f"request: {self.request}\n"
            + f"notes: {self.notes}\n"
            + f"pet_id: {self.pet_id}\n"
            + f"handler_id: {self.handler_id}\n"
        )

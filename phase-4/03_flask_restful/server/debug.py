#!/usr/bin/env python
from models.crew_member import CrewMember
from models.production import Production
from models.__init__ import db
from app import app

if __name__ == "__main__":
    with app.app_context():   
        import ipdb; ipdb.set_trace()
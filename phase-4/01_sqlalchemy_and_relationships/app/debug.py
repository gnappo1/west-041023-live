from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Pet, Owner, metadata, Base, Job, Handler

from datetime import datetime, date, timedelta

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

if __name__ == '__main__':
    engine = create_engine('sqlite:///pet_walker.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    import ipdb; ipdb.set_trace()
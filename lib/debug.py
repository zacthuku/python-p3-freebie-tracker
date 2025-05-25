#!/usr/bin/env python3

from sqlalchemy import create_engine
from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker
 

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Preload objects for easy debugging
    dev = session.query(Dev).first()
    company = session.query(Company).first()
    freebie = session.query(Freebie).first()

    dev1 = session.query(Dev).filter_by(name="Alice").first()
    dev2 = session.query(Dev).filter_by(name="Bob").first()
    freebie = dev1.freebies[0]
    import ipdb; ipdb.set_trace()

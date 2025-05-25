#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie  

engine = create_engine('sqlite:///freebies.db', echo=True)  
Session = sessionmaker(bind=engine)
session = Session()

# Create companies
company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="InnovateLLC", founding_year=2010)

# Create devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

session.add_all([company1, company2, dev1, dev2])
session.commit()

# Create freebies
freebie1 = Freebie(item_name="Sticker Pack", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-shirt", value=50, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Coffee Mug", value=15, dev=dev2, company=company1)

session.add_all([freebie1, freebie2, freebie3])
session.commit()

print("Seeding done!")

session.close()

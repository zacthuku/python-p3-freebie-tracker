from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', back_populates='company')

    devs = relationship(
        'Dev',
        secondary='freebies',
        primaryjoin='Company.id == Freebie.company_id',
        secondaryjoin='Dev.id == Freebie.dev_id',
        viewonly=True
    )

    def give_freebie(self, dev, item_name, value):
        from sqlalchemy.orm.session import object_session
        session = object_session(self)
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()



    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', back_populates='dev')

    companies = relationship(
        'Company',
        secondary='freebies',
        primaryjoin='Dev.id == Freebie.dev_id',
        secondaryjoin='Company.id == Freebie.company_id',
        viewonly=True
    )

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev, freebie):
        from sqlalchemy.orm.session import object_session
        if freebie in self.freebies:
            freebie.dev = other_dev
            session = object_session(freebie)
            session.commit()

    def __repr__(self):
        return f'<Dev {self.name}>'
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)

    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"


    def __repr__(self):
        return f'<Freebie {self.item_name} (Value: {self.value})>'
import alias as al
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapper, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()

class Argument(Base):
    __tablename__ = 'argument' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    framework_id = Column(Integer, ForeignKey('framework.id'))

class Attack(Base):
    __tablename__ = 'attack'
    attacker_id = Column(Integer, ForeignKey('argument.id'), primary_key=True)
    target_id = Column(Integer, ForeignKey('argument.id'), primary_key=True)
    attacker = relationship("Argument", primaryjoin=attacker_id==Argument.id)
    target = relationship("Argument", primaryjoin=target_id==Argument.id)

class Framework(Base):
    __tablename__ = 'framework'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    args = relationship("Argument", backref="framework")
    labs = relationship("Labelling", backref="framework")

class Labelling(Base):
    __tablename__ = 'labelling'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    framework_id = Column(Integer, ForeignKey('framework.id'))

def msql_create():
    engine = create_engine('sqlite:///sqlalchemy_example.db')
    Base.metadata.create_all(engine)
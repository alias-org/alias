import os 
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class ArgumentationFramework(Base):
    __tablename__ = 'ArgumentationFramework'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=True, nullable=True)

class Argument(Base):
    __tablename__ = 'Argument'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    framework_id = Column(Integer, ForeignKey('ArgumentationFramework.id'))
    framework = relationship(ArgumentationFramework)

class Labelling(Base):
    __tablename__ = 'Labelling'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
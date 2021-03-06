#!/usr/bin/python3
"""
Build a ORM: method of associating user-defined Python classes with database
tables, and instances of those classes (objects) with rows in their
corresponding tables.

Relationship apply to State() - parents:

  Class definition of a City and an instance Base
  State class:
    * inherits from Base
    * links to the MySQL table states
    * Class attribute id represents a column of an auto-generated,
      unique integer, can't be null and is a primary key
    * Class attribute name that represents a column of a string with
      maximum 128 characters and can't be null
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from relationship_state import Base, State


# Base = declarative_base()  # Declare a Mapping
class City(Base):
    """ Module to map 'state' table """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

"""
Build a ORM: method of associating user-defined Python classes with database
tables, and instances of those classes (objects) with rows in their
corresponding tables.

  Class definition of a State and an instance Base
  State class:
    * inherits from Base
    * links to the MySQL table states
    * Class attribute id represents a column of an auto-generated,
      unique integer, can't be null and is a primary key
    * Class attribute name that represents a column of a string with maximum 128
      characters and can't be null
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence


Base = declarative_base()  # Declare a Mapping


class State(Base):
    """ Module to map 'state' table """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

    # def __repr__(self):
    #    return "<State(id='%s' name='%s')>" % (self.id, self.name)

#!/usr/bin/python3
"""
Script that creates the State California with the City San Francisco from the
database hbtn_0e_100_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwd, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(engine)
    Session.configure(bind=engine)
    session = Session()

    # instance
    state1 = State(name="California")
    city1 = City(name="San Francisco")
    state1.cities.append(city1)

    # Adding state - city
    session.add(state1)
    session.commit()

    session.close()

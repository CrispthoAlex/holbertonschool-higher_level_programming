#!/usr/bin/python3
"""
Start link class to table in database.
Script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    # create session
    Session = sessionmaker(engine)
    Session.configure(bind=engine)
    session = Session()

    # Save the query in a variable
    query = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)
    # Print query
    for state, city in query:  # .all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

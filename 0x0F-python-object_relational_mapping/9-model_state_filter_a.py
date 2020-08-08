#!/usr/bin/python3
"""
Start link class to table in database.
script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
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

    # Save the query with filter ilike to garantee search specific
    sq = session.query(State).filter(State.name.ilike('%a%'))
    for data in sq.all():
        print("{}: {}".format(data.id, data.name))  # Print query

    session.close()

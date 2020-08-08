#!/usr/bin/python3
"""
Start link class to table in database.
Script that lists all State objects from the database hbtn_0e_6_usa
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

    if session.query(State).first():  # CHECK EMPTY TABLE
        sq = session.query(State).order_by(State.id)  # Save the query
        df = sq.first()  # first data searched
        print("{}: {}".format(df.id, df.name))  # Print query
    else:
        print("Nothing")

    session.close()

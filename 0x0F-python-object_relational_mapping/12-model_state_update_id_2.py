#!/usr/bin/python3
"""
Start link class to table in database.
script that changes the name of a object from the database
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

    chdata = 'Louisiana'  # State name to change on table

    # Save the query with filter by id. Then, update row/data
    # sq = session.query(State).filter(State.name == '{}'.format(st_name))
    sq = session.query(State).filter(State.id == 2).first()
    # Update data/row
    sq.name = "New Mexico"

    # Flush pending changes and commit the current transaction.
    # If no transaction is in progress, this method raises an
    # InvalidRequestError.
    session.commit()

    session.close()

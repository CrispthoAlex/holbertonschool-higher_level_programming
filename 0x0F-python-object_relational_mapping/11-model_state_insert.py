#!/usr/bin/python3
"""
Start link class to table in database.
Script that adds the State object Louisiana to the database hbtn_0e_6_usa
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

    newdata = 'Louisiana'  # State name to query
    row_new = State(name=newdata)
    session.add(row_new)
    session.commit()
    # Save the query with filter by name. Too filter injection
    # sq = session.query(State).filter(State.name == '{}'.format(st_name))
    sq = session.query(State).filter(State.name == '{}'.format(newdata))
    if sq.all():
        for data in sq.all():
            print("{}".format(data.id))  # Print query
    else:
        print("Not found")

    session.close()

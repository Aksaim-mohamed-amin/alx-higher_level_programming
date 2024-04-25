#!/usr/bin/python3
"""
changes the name of a State object from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from model_state import Base, State


if __name__ == "__main__":

    # Connect to Mysql server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables defined by ORM-mapped classes in the database
    Base.metadata.create_all(engine)

    # Create a sessionmaker object
    Session = sessionmaker(bind=engine)

    # Create a new session
    session = Session()

    # Select and Update the state name
    try:
        state = session.query(State).filter(State.id == 2).one()
        state.name = "New Mexico"
        session.commit()

    except NoResultFound:
        print("Not Found")

    # Close the session
    session.close()
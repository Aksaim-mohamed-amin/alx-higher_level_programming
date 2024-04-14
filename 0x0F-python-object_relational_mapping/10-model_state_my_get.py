#!/usr/bin/python3
"""
prints the State id with the name passed as argument from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

    # Query the first state object
    state = session.query(State).filter(State.name == sys.argv[4]).one()

    if state is not None:
        print(state.id)
    else:
        print("Nothing")

    # Close the session
    session.close()

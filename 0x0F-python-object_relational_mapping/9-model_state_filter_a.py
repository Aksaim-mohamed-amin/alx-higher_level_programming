#!/usr/bin/python3
"""
lists all State objects that contain the letter 'a' from the database
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
    states = session.query(State)\
                    .order_by(State.id)\
                    .filter(State.name.like('%a%'))\
                    .all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

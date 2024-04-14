#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database.
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

    # Creating new State object and adding it to the state table
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

    # Close the session
    session.close()

#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL server runing on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables defined by ORM-mapped classes in the database
    Base.metadata.create_all(engine)

    # Create a sessionmaker object
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State obkects and sort by id in asc order
    states = session.query(State).order_by(State.id).all()

    # Print the result
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()

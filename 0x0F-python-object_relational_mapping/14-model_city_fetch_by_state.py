#!/usr/bin/python3
"""
prints all City objects from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State


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

    # Print all the cities in the cities table
    res = session.query(City, State)\
                 .filter(City.state_id == State.id)\
                 .order_by(City.id)\
                 .all()

    for city, state in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()

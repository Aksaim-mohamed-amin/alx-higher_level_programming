#!/usr/bin/python3
"""
prints the State id with the name passed as argument from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Create a new city and add it to database
    new_city = City(name="San Francisco")

    new_state = State(name="California")
    new_state.cities.append(new_city)

    session.add(new_city)
    session.add(new_state)

    session.commit()

    # Close the session
    session.close()

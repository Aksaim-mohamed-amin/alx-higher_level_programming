#!/usr/bin/python3
"""
prints all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(f"mysql://{username}:{password}@localhost/{dbname}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(City,
                                             City.state_id == State.id).all()
    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

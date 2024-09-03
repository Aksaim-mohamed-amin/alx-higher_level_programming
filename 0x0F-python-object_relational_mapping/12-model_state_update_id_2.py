#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_us
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(f"mysql://{username}:{password}@localhost/{dbname}",
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).one_or_none()
    if state:
        state.name = 'New Mexico'
        session.commit()

    session.close()

#!/usr/bin/python3
"""Define a State class and an instance Base for SQLAlchemy ORM"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Represents a state for SQLAlchemy ORM"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

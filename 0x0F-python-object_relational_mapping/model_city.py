#!/usr/bin/python3
"""class definition of a City and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """Cities ORM table object

    Attributes:
        id(int): unique identifier
        name(str): city
        state_id(int): foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

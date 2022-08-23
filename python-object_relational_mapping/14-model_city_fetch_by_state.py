#!/usr/bin/python3
"""
Module 14-model_city_fetch_by_state.py
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(State.name, City.id, City.name).filter(
              State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(ins[0], ins[1], ins[2]))
    session.close()

#!/usr/bin/python3
"""
Module 8-model_state_fetch_first.py
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_ins = session.query(State).order_by(State.id).first()
    if first_ins:
        print("{:d}: {:s}".format(first_ins.id, first_ins.name))
    else:
        print("Nothing")
    session.close()

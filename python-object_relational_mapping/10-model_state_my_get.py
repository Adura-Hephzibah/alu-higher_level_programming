#!/usr/bin/python3
"""
Module 10-model_state_my_get.py
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
    ins = session.query(State).filter_by(name=argv[4]).first()
    if ins:
        print("{:d}".format(ins.id))
    else:
        print("Not found")
    session.close()

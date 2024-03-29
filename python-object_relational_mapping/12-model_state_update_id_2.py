#!/usr/bin/python3
"""
Module 12-model_state_update_id_2.py
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

    change = session.query(State).filter_by(id=2).first()
    change.name = "New Mexico"

    session.commit()

    session.close()

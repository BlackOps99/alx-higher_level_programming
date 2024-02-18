#!/usr/bin/python3
"""
Script that get all state that names has (a)
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    states = Session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    Session.close()

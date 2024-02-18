#!/usr/bin/python3
"""
Script that add new state
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

    state = State(name="Louisiana")

    Session.add(state)
    Session.commit()

    print(state.id)

    Session.close()

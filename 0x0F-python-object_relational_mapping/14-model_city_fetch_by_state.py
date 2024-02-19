#!/usr/bin/python3
"""
Script that lists all city and state name for each sity
"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    citys = Session.query(State, City).join(City).order_by(City.id)

    for state, city in citys:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    Session.close()

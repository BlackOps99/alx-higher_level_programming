#!/usr/bin/python3
"""
Script that add new state and city
"""
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    california = State(name="California", cities=[City(name="Los Angeles")])

    Session.add(california)
    Session.commit()

    Session.close()

#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = argv[1]
    pwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, pwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # this is the class
    session = Session()  # this is the instance

    result = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()

    for state, city in result:
        print("{}: ({}) {}" .format(state.name, city.id, city.name))

    session.close()

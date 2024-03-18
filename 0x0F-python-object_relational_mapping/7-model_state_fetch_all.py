#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
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

    res = session.query(State).order_by(State.id)
    for state in res:
        print("{}: {}".format(state.id, state.name))

    session.close()

#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
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

    Session = sessionmaker(bind=engine)  # this is the class
    session = Session()  # this is the instance

    states = session.query(State).filter(
        State.name.like("%a%")).all()

    for s in states:
        session.delete(s)

    session.commit()
    session.close()

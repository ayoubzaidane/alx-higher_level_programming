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

    first = session.query(State).order_by(State.id).first()
    if first:
        print("{:d}: {:s}".format(first.id, first.name))
    else:
        print("Nothing")

    session.close()

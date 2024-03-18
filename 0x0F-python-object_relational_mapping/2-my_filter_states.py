#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM states
    WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4]))

    result = cursor.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    conn.close()

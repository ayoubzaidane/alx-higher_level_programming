#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state
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

    query = """SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC"""

    cursor.execute(query, (argv[4],))

    result = cursor.fetchall()

# format the printing of cities of same state separated by commas
    print(', '.join(["{:s}".format(row[0]) for row in result]))
    cursor.close()
    conn.close()

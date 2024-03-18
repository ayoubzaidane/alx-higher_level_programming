#!/usr/bin/python3
"""
lists all states with a name starting with N
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

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    result = cursor.fetchall()

    for row in result:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    conn.close()

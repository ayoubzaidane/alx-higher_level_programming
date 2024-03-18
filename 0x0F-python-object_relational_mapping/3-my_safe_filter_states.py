#!/usr/bin/python3
"""
return matching states; safe from MySQL injections
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

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))

    result = cursor.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    conn.close()

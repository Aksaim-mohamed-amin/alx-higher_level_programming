#!/usr/bin/python3
""" lists all states from the database """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor
    cursor = db.cursor()

    # Execute the command in SQL
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Retrive the result
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close connection
    cursor.close()
    db.close()

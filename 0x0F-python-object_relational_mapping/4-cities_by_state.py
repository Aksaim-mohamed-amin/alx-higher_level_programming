#!/usr/bin/python3
""" lists all cities from database """

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
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id""")

    # Retrive the result
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close connection
    cursor.close()
    db.close()

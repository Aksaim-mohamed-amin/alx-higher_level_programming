#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

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
    cursor.execute("""
    SELECT cities.name
    FROM cities JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """, (state,))

    # Retrive the result
    cities = cursor.fetchall()
    cities_list = [city[0] for city in cities]
    print(', '.join(cities_list))

    # Close connection
    cursor.close()
    db.close()

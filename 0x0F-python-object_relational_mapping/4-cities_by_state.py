#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    connection = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cur = connection.cursor()
    cur.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities JOIN states
    ON cities.state_id=states.id
    ORDER BY cities.id
    """)

    cities = cur.fetchall()
    for row in cities:
        print(row)

    cur.close()
    connection.close()

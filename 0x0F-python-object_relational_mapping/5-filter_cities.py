#!/usr/bin/python3
"""
List all cities of a state from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    cur = connection.cursor()
    cur.execute("""
    SELECT cities.name
    FROM cities JOIN states
    ON cities.state_id=states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """, (state_name,))

    result = cur.fetchall()
    cities = [row[0] for row in result]
    print(', '.join(cities))

    cur.close()
    connection.close()

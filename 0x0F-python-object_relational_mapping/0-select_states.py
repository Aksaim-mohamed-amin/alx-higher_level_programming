#!/usr/bin/python3
"""Connect to hbtn_0e_0_usa database and lists all states"""

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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    connection.close()

#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
    * Your script should take 3 arguments: mysql username, mysql password and
      database name
    * You must use the module MySQLdb (import MySQLdb)
    * Your script should connect to a MySQL server running on localhost at
      port 3306
    * Results must be sorted in ascending order by cities.id
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # parameters
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    # state = argv[4]

    # Connecting to a MySQL database
    database = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=passwd, db=db_name)
    # Getting a Cursor in MySQL: ability to have multiple seperate working
    # environments through the same connection to the database
    curtodb = database.cursor()  # cursor to database
    # String for Query. Use decode() to decoding form bin to char/string
    # SEARCH sq = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".
    # format(MySQLdb.escape_string(state).decode())
    sq = "SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY id ASC;"
    # Executing MySQL Queries
    curtodb.execute(sq)
    # Obtaining Query Results
    rows = curtodb.fetchall()
    for data in rows:
        print(data)

    curtodb.close()  # Close Cursor in MySQL
    database.close()  # Close Connecting to a MySQL database

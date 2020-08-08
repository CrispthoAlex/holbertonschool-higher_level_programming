#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
    state_name = argv[4]

    # Connecting to a MySQL database
    database = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=passwd, db=db_name)

    # Getting a Cursor in MySQL: ability to have multiple seperate working
    # environments through the same connection to the database
    curtodb = database.cursor()  # cursor to database

    # String for Query. Use decode() to decoding form bin to char/string
    # code line to injection: format(MySQLdb.escape_string("var").decode())
    sq = "\
    SELECT cities.name FROM cities INNER JOIN states \
    ON cities.state_id = states.id \
    WHERE states.name = '{}' \
    ORDER BY cities.id ASC;".format(MySQLdb.escape_string(state_name).decode())

    # Executing MySQL Queries
    curtodb.execute(sq)

    # Obtaining Query Results
    rows = curtodb.fetchall()

    # Using list comprehension to print
    print(", ".join(data[0] for data in rows))

    curtodb.close()  # Close Cursor in MySQL
    database.close()  # Close Connecting to a MySQL database

#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # parameters
    username = argv[1]  # User name: root
    passwd = argv[2]  # User password
    db_name = argv[3]  # Database name
    state = argv[4]  # State name or Argument to seacrh in table

    # Connecting to MySQL database
    database = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=passwd, db=db_name)
    # Getting a Cursor in MySQL: ability to have multiple seperate working
    # environments through the same connection to the database
    curtodb = database.cursor()  # cursor to database
    # String for Query with LIKE BINARY to avoid sensitive
    sq = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
    ORDER BY id ASC".format(state)
    # Executing MySQL Queries
    curtodb.execute(sq)
    # Obtaining Query Results
    rows = curtodb.fetchall()
    for data in rows:
        print(data)

    curtodb.close()  # Close Cursor in MySQL
    database.close()  # Close Connecting to MySQL database

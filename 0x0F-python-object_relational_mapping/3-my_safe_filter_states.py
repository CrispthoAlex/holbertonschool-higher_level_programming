#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But write one that is
safe from MySQL injections!
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # parameters
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state = argv[4]

    # Connecting to a MySQL database
    database = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=passwd, db=db_name)
    # Getting a Cursor in MySQL: ability to have multiple seperate working
    # environments through the same connection to the database
    curtodb = database.cursor()  # cursor to database
    # String for Query. Use decode() to decoding form bin to char/string
    sq = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        MySQLdb.escape_string(state).decode())
    # Executing MySQL Queries
    curtodb.execute(sq)
    # Obtaining Query Results
    rows = curtodb.fetchall()
    for data in rows:
        print(data)

    curtodb.close()  # Close Cursor in MySQL
    database.close()  # Close Connecting to a MySQL database

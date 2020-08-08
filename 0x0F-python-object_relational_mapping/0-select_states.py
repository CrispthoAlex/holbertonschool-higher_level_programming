#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # parameters
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    # Connecting to a MySQL database
    database = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=passwd, db=db_name)
    # Getting a Cursor in MySQL: ability to have multiple seperate working
    # environments through the same connection to the database
    curtodb = database.cursor()  # cursor to database
    # Executing MySQL Queries
    curtodb.execute("SELECT * FROM states ORDER BY id ASC")
    # Obtaining Query Results
    rows = curtodb.fetchall()
    for data in rows:
        print(data)

    curtodb.close()  # Close Cursor in MySQL
    database.close()  # Close Connecting to a MySQL database

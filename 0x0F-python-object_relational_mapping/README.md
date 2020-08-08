# 0x0F. Python - Object-relational mapping

Please make sure your MySQL server is in 5.7 -> How to install MySQL 5.7 in Ubuntu 14.04

# Background Context
In this project, we will link two amazing worlds: Databases and Python!

In the first part, we will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, we will use the module SQLAlchemy (dont ask me how to pronounce it) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be What can I do with my objects and not How this object is stored? where? when?. You wont write any SQL queries only Python code. Last thing, your code wont be storage type dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
````
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
````
With an ORM:

````
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
````

# Resources
#### Read or watch:

* Object-relational mappers
* mysqlclient/MySQLdb documentation (please dont pay attention to _mysql)
* MySQLdb tutorial
* SQLAlchemy tutorial
* SQLAlchemy
* mysqlclient/MySQLdb
* Introduction to SQLAlchemy
* Flask SQLAlchemy
* 10 common stumbling blocks for SQLAlchemy newbies
* Python SQLAlchemy Cheatsheet
* SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)

# Learning Objectives
## General
* Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

# More Info
### Install ``MySQLdb`` module version ``1.3.x``
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 5.7 in Ubuntu 14.04

#### Install MySQL 5.7 on Ubuntu 14.04 LTS
````
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
````
#### Install MySQLdb
````
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__
'1.3.10'
````

#### Install SQLAlchemy module version 1.2.x
````
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.2.5'
````
Also, you can have this warming message:
````
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
    cursor.execute(statement, parameters)
````
You can ignore it.

# Tasks

0. Get all states
1. Filter states
2. Filter states by user input
3. SQL Injection...
4. Cities by states
5. All cities by state
6. First state model
7. All states via SQLAlchemy
8. First state
9. Contains `a`
10. Get a state
11. Add a new state
12. Update a state
13. Delete states
14. Cities in state

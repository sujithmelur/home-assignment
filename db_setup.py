#!/usr/bin/python

import mysql.connector as mariadb

db_connection=mariadb.connect(user='root',password='')

cursor = db_connection.cursor()

cursor.execute("CREATE USER 'wiki'@'localhost' IDENTIFIED BY 'DbPasswd';")
cursor.execute("CREATE DATABASE wikidatabase")
cursor.execute("GRANT ALL PRIVILEGES ON wikidatabase.* TO 'wiki'@'localhost';")
cursor.execute("FLUSH PRIVILEGES;")

cursor.execute("SHOW DATABASES")



for db in cursor:
   print(db)
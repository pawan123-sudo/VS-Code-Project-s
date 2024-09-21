import sqlite3

# create database
Database = sqlite3.connect("Database.db")

# show the message of datebase creation
print("created the database")

# create cursur
cursor = Database.cursor()

# insert in Database


cursor.close()
# this file makes calls to the DB named tables.db
# SQLite3 is not case sensitive with table names (ie. tables are created lowercase, called here in CamelCase)

import sqlite3
import re

from datetime import datetime

DB = None
CONN = None

def add_new_user(email, password):
    query = """INSERT INTO Users VALUES (?,?)"""
    DB.execute(query, (email, password))
    CONN.commit()
    return "Successfully added user!" 

def add_new_post(title, body, user_id, datestamp):
    query = """INSERT INTO Posts (title, body, user_id, created_at) VALUES (?,?,?,?)"""
    DB.execute(query, (title, body, user_id, datetime.now()))
    CONN.commit()
    return "Successfully added post!"

def view_all_posts():
    query = """SELECT * FROM Posts"""
    DB.execute(query, ())
    posts = DB.fetchall()
    return posts

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("tables.db")
    DB = CONN.cursor()

if __name__ == "__main__":
    main()
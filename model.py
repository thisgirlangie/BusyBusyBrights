# this file makes calls to the DB named tables.db
# SQLite3 is not case sensitive with table names (ie. tables are created lowercase, called here in CamelCase)

import sqlite3
import re

DB = None
CONN = None

def add_new_user(id, email, password):
    query = """INSERT INTO Users VALUES (?,?,?)"""
    DB.execute(query, (id, email, password))
    CONN.commit()
    return "Successfully added user #%s!" % (id)

def add_new_post(id, title, body, user_id, created_at):
    query = """INSERT INTO Posts VALUES (?,?,?,?,?)"""
    DB.execute(query, (id, title, body, user_id, created_at))
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
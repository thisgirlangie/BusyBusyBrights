# this file makes calls to the DB named tables.db
# SQLite3 is not case sensitive with table names (ie. tables are created lowercase, called here in CamelCase)

import sqlite3
import re

from datetime import datetime

DB = None
CONN = None

# Event class will send back for each event items from both posts and votes tables
# One class per table and create defs for each action (ie. get a user by ID)

class User(object):
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
    
def add_new_user(email, password):
    query = """INSERT INTO Users (email, password) VALUES (?,?)"""
    DB.execute(query, (email, password))
    CONN.commit()

# normally classes go into separate files, but this is a small exercise
class Post(object):
    def __init__(self, id, title, body, user_id, created_at):
        self.id = id
        self.title = title
        self.body = body
        self.user_id = user_id
        self.created_at = created_at

    def get_votes(self):
        query = "SELECT SUM (value) FROM Votes WHERE post_id=?"
        vote = DB.execute(query, (self.id)) # ValueError: parameters are of unsuported type
        # need to convert database output (SUM (1) | --- | 1) into something returnable
        return vote

def add_new_post(title, body, user_id, datestamp):
    query = """INSERT INTO Posts (title, body, user_id, created_at) VALUES (?,?,?,?)"""
    DB.execute(query, (title, body, user_id, datetime.now()))
    CONN.commit()

def view_all_posts():
    query = """SELECT * FROM Posts"""
    DB.execute(query, ())
    posts = DB.fetchall()
    # convert database output to classes
    list_of_posts = []
    for post in posts:
        post = Post(post[0], post[1], post[2], post[3], post[4])
        list_of_posts.append(post)
    return list_of_posts

class Vote(object):
    def __init__(self, id, user_id, post_id, value):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.value = value

def vote():
    query = """INSERT INTO Votes (user_id, post_id, value) VALUES (?,?,?)"""
    DB.execute(query, (user_id, post_id, value))
    CONN.commit()

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("tables.db")
    DB = CONN.cursor()

if __name__ == "__main__":
    main()
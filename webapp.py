# Flask project: What would Hackbrights do?
# Takes in posts (ie. ideas for events) by users
# Lets users vote on them
# Sorts by date (ie. view by today, tomorrow)

# Requirements: 
# (1) Make user
# (2) Log in as user to add post (or, to add post, must log in as user)
# (3) Log in as user to vote (or, to vote, must log in as user)

# Webpages Required:
# User_Add
# User_Log_In
# Post_Add 
# Vote_Add

from flask import Flask, render_template, request

import model

app = Flask(__name__)

# FRONTPAGE OF EVENTS (VIEW ALL)
@app.route("/")
def view_all_events():
    model.connect_to_db()
    posts = model.view_all_posts()
    html = render_template("events.html", posts=posts)
    return html

if __name__ == "__main__":
    app.run(debug=True)
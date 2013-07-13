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

# ADD USER
@app.route("/register")
def view_add_user_form():
    html = render_template("add_user.html")
    return html

@app.route("/add_new_user")
def add_user():
    model.connect_to_db()
    email = request.args.get("email")
    password = request.args.get("password")
    user = model.add_new_user(email, password)
    return "Successfully added a user!"

# ADD EVENT
@app.route("/add_event")
def view_add_event_form():
    html = render_template("add_event.html")
    return html

@app.route("/add_event_fx")
def add_event():
    model.connect_to_db()
    title = request.args.get("title")
    body = request.args.get("body")
    user_id = request.args.get("user_id")
    created_at = request.args.get("datestamp")
    event = model.add_new_post(title, body, user_id, created_at)
    return "Successfully added an event!"

if __name__ == "__main__":
    app.run(debug=True)
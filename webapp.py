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
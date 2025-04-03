from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

#below app declaration
@app.route("/about")
def about():
    return render_template("about.html")

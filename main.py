import flask

app = flask.Flask(__name__)

@app.route("/")
def start():
    return flask.render_template("start.html")

@app.route("/player")
def player():
    return flask.render_template("player.html")

@app.route("/sales")
def sales():
    return flask.render_template("sales.html")

@app.route("/voice")
def voice():
    return flask.render_template("voice.html")

@app.route("/stars")
def stars():
    return flask.render_template("stars.html")

app.run(debug=True)

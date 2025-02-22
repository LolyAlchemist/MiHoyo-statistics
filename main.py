import flask

app = flask.Flask(__name__)

@app.route("/")
def start():
    return flask.render_template("start.html")

@app.route("/player")
def player():
    return flask.render_template("player.html")


app.run(debug=True)

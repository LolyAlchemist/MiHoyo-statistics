import flask

app = flask.Flask(__name__)

@app.route("/")
def start():
    return flask.render_template("start.html")

@app.route("/")
def player():
    return flask.render.template("player.html")
app.run()

import flask
from flask_peewee.db import Database
from flask_peewee.auth import Auth
from peewee import TextField, IntegerField, FloatField

from werkzeug.utils import secure_filename

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, FloatField as FF
from wtforms.validators import DataRequired, Length, EqualTo

DATABASE = {
    'name': 'mihoyo.db',
    'engine': 'peewee.SqliteDatabase'
}
app = flask.Flask(__name__) 
app.config.from_object(__name__)

db = Database(app)
auth = Auth(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route("/")
def base():
    return flask.render_template("base.html")

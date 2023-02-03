
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'auth_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app,db)
primary_key = True

class User_db(db.Model):
    id = db.Column(db.Integer, primary_key  = True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self,username,password):
        self.username=username
        self.password=password


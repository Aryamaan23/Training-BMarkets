import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app,db)

class Pet(db.Model):
    __tablename__='pets'
    pet_id=db.Column(db.Integer,primary_key=True)
    pet_breed=db.Column(db.Text)
    pet_name=db.Column(db.Text)
    pet_owner=db.Column(db.Text)
    pet_age=db.Column(db.Integer)

    def __init__(self,breed,name,owner,age):
        self.pet_breed=breed
        self.pet_name=name
        self.pet_owner=owner
        self.pet_age=age

    def __repr__(self):
        return f"{self.pet_name} is of {self.pet_breed} breed and it's age is {self.pet_age} and it's owner name  is {self.pet_owner}"

"""
if __name__=="__main__":
    app.run(debug=True,port=4343)

"""
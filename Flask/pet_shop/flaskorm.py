import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
from flask import Flask, render_template,request,redirect,url_for

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

    def __init__(self,pet_breed,pet_name,pet_owner,pet_age):
        self.pet_breed=pet_breed
        self.pet_name=pet_name
        self.pet_owner=pet_owner
        self.pet_age=pet_age

    def __repr__(self):
        return f"{self.pet_name} is of {self.pet_breed} breed and it's age is {self.pet_age} and it's owner name  is {self.pet_owner}"


# Imports and CarsModel truncated

@app.route('/pet', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = Pet(pet_breed=data['pet_breed'],pet_name=data['pet_name'],pet_owner=data['pet_owner'],
            pet_age=data['pet_age'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.pet_name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cars = Pet.query.all()
        results = [
            {
                "pet_id":car.pet_id,
                "pet_breed":car.pet_breed,
                "pet_name": car.pet_name,
                "pet_owner": car.pet_owner,
                "pet_age": car.pet_age
            } for car in cars]

        return {"count": len(results), "cars": results}


if __name__=="__main__":
    app.run(debug=True,port=4343)

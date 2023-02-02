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
primary_key = True

#making pet model
'''
class Pet(db.Model):
    _tablename_ = 'pets'
    pet_id    = db.Column(db.Integer, primary_key = True)
    pet_breed = db.Column(db.Text)
    pet_name  = db.Column(db.Text)
    pet_owner = db.Column(db.Text)
    pet_age   = db.Column(db.Integer)

    def _init_(self,breed,name,owner,age):
        self.pet_breed = breed
        self.pet_name = name
[10:06, 02/02/2023] Akshit Khamesra: self.pet_owner = owner
        self.pet_age = age
    def _repr_(self):
        return f"{self.pet_name} is of {self.pet_breed} breed and it's age is {self.pet_age} year old and its owner name is {self.pet_owner}"
    '''
#RELATION
class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    toys = db.relationship('Toy',backref = 'pet', lazy = 'dynamic')
    owner = db.relationship('Owner',backref = 'pet',uselist = False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Pet's name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Pet's name is {self.name} and his owner is not assigned yet!"
    def represent_toys(self):
        print("These are my toys: ")
        for toy in self.toys:
            print(toy.item_name)
    

    
class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))

    def __init__(self,item_name, pet_id):
        self.item_name = item_name
        self.pet_id = pet_id
    
    def __repr__(self):
        return f"These are my toys :{self.item_name}"

class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    
    def __init__(self,name,pet_id):
        self.name= name
        self.pet_id = pet_id

if __name__ == '__main__':
    app.run(debug=True)

"""
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

"""

from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SelectField,DateTimeField,TextAreaField,SubmitField,RadioField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class Pet(FlaskForm):
    pet_types=[('Dog','Dog'),('Cat','Cat'),('Cow','Cow')]
    owner_name=StringField('Name')
    pet_name=StringField('PetName')
    pet_type= SelectField('Type', choices=pet_types)
    dateofadoption=StringField('Date of Adoption')


"""
 'name varchar (150) NOT NULL,'
                                 'pet_name varchar (50) NOT NULL,'
                                 'pet_type varchar (50) NOT NULL,'
                                 'date_of_adoption date DEFAULT CURRENT_TIMESTAMP);'

"""
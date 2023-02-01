import os
import psycopg2
from flask import Flask, render_template,request,redirect,url_for
from petshop1_models import Pet


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='postgres',
                            password='Finserv@2023')
    return conn
#When we connect to a remote server 2 more things are required that is port=5432 and ip address

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM owner;')
    owner_details = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('petshop1.html', owner_details=owner_details)

"""
class Pet(FlaskForm):
    pet_types=[('Dog','Dog'),('Cat','Cat'),('Cow','Cow')]
    o_name=StringField('Name')
    pet_name=StringField('PetName')
    pet_type= SelectField('Type', choices=pet_types)
    dateofadoption=StringField('Date of Adoption')

cur.execute('INSERT INTO owner (name, pet_name, pet_type)'
            'VALUES (%s, %s, %s)',
            ('Aryamaan Pandey',
             'Tom',
             'Dog',
            )
            )

"""

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['owner_name']
        pet_name = request.form['pet_name']
        pet_type = request.form['pet_type']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO owner (name,pet_name,pet_type)'
                    'VALUES (%s, %s, %s)',
                    (name, pet_name, pet_type))
        #It's important otherwise you won't be able to see the changes!
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('petshopcreate.html')


@app.route('/delete/<int:ids>')
def delete(ids):
    conn = get_db_connection()
    curr = conn.cursor()
    t = (ids,)
    curr.execute('DELETE FROM owner WHERE oid = %s', (ids,))
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/error')
def error():
    return redirect('error.html',error=error)


if __name__ == '__main__':
    app.run(debug=True)
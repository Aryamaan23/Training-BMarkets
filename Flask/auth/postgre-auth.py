from flask import Flask,render_template,request,redirect
import requests
app = Flask(__name__)
import datetime
import json
import string
from random import choice


@app.route('/register',methods=["GET","POST"])
def register():
    return render_template('register.html')

if __name__=="__main__":
    app.run(debug=True)
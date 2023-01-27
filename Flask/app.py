#WSGI

from flask import Flask,render_template
app = Flask(__name__)
import datetime

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/educative")
def learn():
    return "Happy Learning at Educative!"

@app.route("/temp")
def temp():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
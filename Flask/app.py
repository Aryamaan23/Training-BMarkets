#WSGI

from flask import Flask,render_template,request
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
    return render_template('index.html',utc_dt=datetime.datetime.now())

@app.route("/req")
def req():
    browser_info=request.headers.get('User-Agent')
    return f'<h2>Where is your browser info: </h2> <p>{browser_info}</p>'

#For passing the variable to the route
@app.route("/user/<name>")
def user(name):
    return f"<h1>This is a page for user: {name.upper()} </h1>"

if __name__ == '__main__':
    app.run()
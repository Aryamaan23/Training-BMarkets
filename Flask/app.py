#WSGI

from flask import Flask,render_template,request,redirect
import requests
app = Flask(__name__)
import datetime
import json
import string
from random import choice
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

@app.route("/age/<int:age>")
def age(age):
    return render_template('age.html',age=age)

#For passing the variable to the route
@app.route("/user/<name>")
def user(name):
    return f"<h1>This is a page for user: {name.upper()} </h1>"

@app.route("/user_latin/<name>")
def userlatin(name):
    #user Latin the name that comes in!
    username=" "
    if name[-1]=='y':
        username=name[:-1] + 'iful'
    else:
        username=name+'y'
    return f"<h1> Hi {name}! Your user latin name is {username} </h1>"


#Method 1
@app.route("/url_shorten/<urlo>")
def shorten_url(urlo):
    url = "https://api.apilayer.com/short_url/hash"
    payload = urlo.encode("utf-8")
    headers= {
         "apikey": "20dliytiGk0QY1dQsEGE9wnSK3uG8iq9"
        }
    response = requests.request("POST", url, headers=headers, data = payload)
    status_code = response.status_code
    result = response.text
    result=json.loads(result)
    return f"<h1>Your shortened url is : <a href='{result['short_url']}'>{result['short_url']} </a></h1>"



d={}


def generate_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

@app.route('/urlshortener/<url>')
def short(url):
    surl=generate_id(4)
    d[surl]=url
    if url not in d.values():
        d[surl]=surl
    #return request.host_url+surl
    print(type(d))
    return d

@app.route('/<id>')
def url_redirect(id):
    original_url=d[id]
    # print(original_url)
    return redirect(d[id],code=302)


if __name__ == '__main__':
    app.run(debug=True)
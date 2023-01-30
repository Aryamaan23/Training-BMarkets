from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SelectField,DateTimeField,TextAreaField,SubmitField,RadioField

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):
    breed=StringField("What breed are you?")
    submit=SubmitField("Submit")

@app.route("/",methods=["GET","POST"])
def index():
    form=InfoForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash(f"You first changed your breed to: {session['breed']}")
        return redirect(url_for("index"))
    return render_template('home4.html',form=form)

if __name__=='__main__':
    app.run(debug=True,port=2311)
from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SelectField,DateTimeField,TextAreaField,SubmitField,RadioField
from wtforms.validators import DataRequired
app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class SimpleForm(FlaskForm):
    submit=SubmitField("Click me!")
    

@app.route("/",methods=['GET','POST'])
def index():
    form=SimpleForm()
    if form.validate_on_submit():
        flash("You just clicked the button!")
        return redirect(url_for('thankyou3'))
    return render_template('flasho.html',form=form)


@app.route("/thankyou3")
def thankyou3():
    return render_template("thankyou3.html")

if __name__=='__main__':
    app.run(debug=True,port=7000)
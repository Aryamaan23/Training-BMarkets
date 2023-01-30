from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SelectField,DateTimeField,TextAreaField,SubmitField,RadioField
from wtforms.validators import DataRequired
app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):
    breed=StringField("What breed are you? ",validators=[DataRequired()])
    tomcat=BooleanField("Have you been tomcat?")
    mood=RadioField("Please choose your mood : ",choices=[('mood_one','bad'),('mood_two','good')])
    food_choice=SelectField(u'Pick your favourite food: ',choices=[('chi','Chicken'),('bef','beef'),('fish','FISH')])
    feedback=TextAreaField()
    submit=SubmitField("Submit")

@app.route("/",methods=['GET','POST'])
def index():
    form=InfoForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        session['tomcat']=form.tomcat.data
        session['mood']=form.mood.data
        session['food_choice']=form.food_choice.data
        session['feedback']=form.feedback.data
        return redirect(url_for('thankyou2'))
    return render_template('info.html',form=form)


@app.route("/thankyou2")
def thankyou2():
    return render_template("thankyou2.html")

if __name__=='__main__':
    app.run(debug=True,port=7000)
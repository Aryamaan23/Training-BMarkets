from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
app=Flask(__name__)
app.config['SECRET_KEY']="mysecretkey"#We are generating this CSRF token 

class TestForm(FlaskForm):
    cat_breed=StringField('What is cat breed?')
    submit=SubmitField('Submit')

@app.route("/",methods=['GET','POST'])
def index():
    cat_breed=False
    form=TestForm()
    if form.validate_on_submit():
        cat_breed=form.cat_breed.data
        #form.cat_breed=" "
        
    return render_template('cat.html',cat_breed=cat_breed,form=form)
       

if __name__=="__main__":
    app.run(debug=True,port=5000)

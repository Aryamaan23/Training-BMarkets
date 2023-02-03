from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate,identity
from flask_jwt import JWT,jwt_required
from umodel import app

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
api = Api(app)
jwt=JWT(app,authenticate,identity)

cats=[]





class CatNames(Resource):
    @jwt_required()
    def get(self,name):
        print(cats)
        for cat in cats:
            if cat.get('name')==name:
                return cat
        return {'name': "No cats found"},404
    
    @jwt_required()
    def post(self,name):
        cat={'name':name}
        cats.append(cat)
        print(cat)
        return cat

    @jwt_required()
    def delete(self,name):
        for index,cat in enumerate(cats):
            if cat.get('name')==name:
                de=cats.pop(index)
                return {'name' : 'delete message'}
        return {'name' : 'not found to delete'}
api.add_resource(CatNames,'/cat/<string:name>')

class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {'cats':cats}


api.add_resource(AllNames,'/cats')

class Hello(Resource):
    def get(self):
        return {'hi' : 'hello'}

api.add_resource(Hello, "/")

if __name__ == "__main__":
    app.run(debug=True, port=1300)
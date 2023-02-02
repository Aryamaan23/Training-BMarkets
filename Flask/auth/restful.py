from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

cats=[]

class CatNames(Resource):
    def get(self,name):
        print(cats)
        for cat in cats:
            if cat.get('name')==name:
                return cat
        return {'name': "No cats found"},404

    def post(self,name):
        cat={'name':name}
        cats.append(cat)
        print(cat)
        return cat

    def delete(self,name):
        for index,cat in enumerate(cats):
            if cat.get('name')==name:
                de=cats.pop(index)
                return {'name' : 'delete message'}
        return {'name' : 'not found to delete'}
api.add_resource(CatNames,'/cat/<string:name>')

class AllNames(Resource):
    def get(self):
        return {'cats':cats}


api.add_resource(AllNames,'/cats')

class Hello(Resource):
    def get(self):
        return {'hi' : 'hello'}

api.add_resource(Hello, "/")

if __name__ == "__main__":
    app.run(debug=True, port=1300)
from flask import Flask, app, jsonify,request
from flask_restful import Api,Resource,reqparse,abort
from flask_pymongo import pymongo
import db_config as database

app=Flask(__name__)
api=Api(app)

class Test(Resource):
    def get(self):
        return jsonify({"message":"Connected"})

class Badge(Resource):
    def post(self):
        database.db.Badge.insert_one({
            'HeaderBackground': request.json['HeaderBackground'],
            'ProfilePic':request.json['ProfilePic'],
            'name':request.json['name'],
            'age':request.json['age'],
            'city':request.json['city'],
            'games':request.json['games'],
            'achievements':request.json['achievements'],
            'followers':request.json['followers']
        })

class AllBadge(Resource):
    """Get all badges"""
    def get(self):
        pass

api.add_resource(Badge,'/new/')
api.add_resource(Test,'/test/')


if __name__ == '__main__':
    app.run(load_dotenv=True)
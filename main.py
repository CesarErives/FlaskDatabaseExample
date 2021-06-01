from flask import Flask, app, json, jsonify,request
from flask.wrappers import Response
from flask_restful import Api,Resource,reqparse,abort
from flask_pymongo import pymongo
from bson.json_util import dumps,ObjectId
import db_config as database

app=Flask(__name__)
api=Api(app)

class Test(Resource):
    def get(self):
        return jsonify({"message":"Connected"})

class Badge(Resource):

    def get(self,by,data):
        response = self.abort_if_not_exist(by,data)
        response['_id'] = str(response['_id'])
        return jsonify(response)


    def post(self):
        _id = str(database.db.Badge.insert_one({
            'HeaderBackground': request.json['HeaderBackground'],
            'ProfilePic':request.json['ProfilePic'],
            'name':request.json['name'],
            'age':request.json['age'],
            'city':request.json['city'],
            'games':request.json['games'],
            'achievements':request.json['achievements'],
            'followers':request.json['followers']
        }).inserted_id)
        return jsonify({"_id":_id})

    def put(self,by,data):
        response=self.abort_if_not_exist(by,data)

        for key,value in request.json.items():
            response[key] = value
        
        database.db.Badge.update_one({'_id':ObjectId(response['_id'])}, 
        {'$set':{
            'HeaderBackground': response['HeaderBackground'],
            'ProfilePic':response['ProfilePic'],
            'name':response['name'],
            'age':response['age'],
            'city':response['city'],
            'games':response['games'],
            'achievements':response['achievements'],
            'followers':response['followers']
        }})
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def abort_if_not_exist(self,by,data):
        if by == "_id":
            response = database.db.Badge.find_one({"_id":ObjectId(data)})
        else:
            response = database.db.Badge.find_one({f"{by}":data})

        if response:
            return response
        else:
            abort(jsonify({"Status":404, f"{by}":f"{data} not found"}))

class AllBadge(Resource):
    """Get all badges"""
    def get(self):
        pass

api.add_resource(Badge,'/new/','/<string:by>=<string:data>/')
api.add_resource(Test,'/test/')


if __name__ == '__main__':
    app.run(load_dotenv=True)
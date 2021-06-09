from flask import json, jsonify,request
from flask_restful import Resource,abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
from werkzeug.wrappers import response
import db_config as database

class Badges(Resource):
    """Get all badges"""
    def get(self):
        response = list(database.db.Badge.find())

        for doc in response:
            doc['id'] = str(doc['_id'])

        return jsonify(response)

    def post(self):
        _ids = list(
            database.db.Badge.insert_many([
                {
            'HeaderBackground': request.json[0]['HeaderBackground'],
            'ProfilePic':request.json[0]['ProfilePic'],
            'name':request.json[0]['name'],
            'age':request.json[0]['age'],
            'city':request.json[0]['city'],
            'games':request.json[0]['games'],
            'achievements':request.json[0]['achievements'],
            'followers':request.json[0]['followers']
                },
                {
            'HeaderBackground': request.json[1]['HeaderBackground'],
            'ProfilePic':request.json[1]['ProfilePic'],
            'name':request.json[1]['name'],
            'age':request.json[1]['age'],
            'city':request.json[1]['city'],
            'games':request.json[1]['games'],
            'achievements':request.json[1]['achievements'],
            'followers':request.json[1]['followers']

                },
                {
            'HeaderBackground': request.json[2]['HeaderBackground'],
            'ProfilePic':request.json[2]['ProfilePic'],
            'name':request.json[2]['name'],
            'age':request.json[2]['age'],
            'city':request.json[2]['city'],
            'games':request.json[2]['games'],
            'achievements':request.json[2]['achievements'],
            'followers':request.json[2]['followers']
                },
                {
            'HeaderBackground': request.json[3]['HeaderBackground'],
            'ProfilePic':request.json[3]['ProfilePic'],
            'name':request.json[3]['name'],
            'age':request.json[3]['age'],
            'city':request.json[3]['city'],
            'games':request.json[3]['games'],
            'achievements':request.json[3]['achievements'],
            'followers':request.json[3]['followers']
                },
                {
            'HeaderBackground': request.json[4]['HeaderBackground'],
            'ProfilePic':request.json[4]['ProfilePic'],
            'name':request.json[4]['name'],
            'age':request.json[4]['age'],
            'city':request.json[4]['city'],
            'games':request.json[4]['games'],
            'achievements':request.json[4]['achievements'],
            'followers':request.json[4]['followers']
                },
                {
            'HeaderBackground': request.json[5]['HeaderBackground'],
            'ProfilePic':request.json[5]['ProfilePic'],
            'name':request.json[5]['name'],
            'age':request.json[5]['age'],
            'city':request.json[5]['city'],
            'games':request.json[5]['games'],
            'achievements':request.json[5]['achievements'],
            'followers':request.json[5]['followers']
                },
                {
            'HeaderBackground': request.json[6]['HeaderBackground'],
            'ProfilePic':request.json[6]['ProfilePic'],
            'name':request.json[6]['name'],
            'age':request.json[6]['age'],
            'city':request.json[6]['city'],
            'games':request.json[6]['games'],
            'achievements':request.json[6]['achievements'],
            'followers':request.json[6]['followers']
                },
                {
            'HeaderBackground': request.json[7]['HeaderBackground'],
            'ProfilePic':request.json[7]['ProfilePic'],
            'name':request.json[7]['name'],
            'age':request.json[7]['age'],
            'city':request.json[7]['city'],
            'games':request.json[7]['games'],
            'achievements':request.json[7]['achievements'],
            'followers':request.json[7]['followers']
                },
                {
            'HeaderBackground': request.json[8]['HeaderBackground'],
            'ProfilePic':request.json[8]['ProfilePic'],
            'name':request.json[8]['name'],
            'age':request.json[8]['age'],
            'city':request.json[8]['city'],
            'games':request.json[8]['games'],
            'achievements':request.json[8]['achievements'],
            'followers':request.json[8]['followers']
                },
                {
            'HeaderBackground': request.json[9]['HeaderBackground'],
            'ProfilePic':request.json[9]['ProfilePic'],
            'name':request.json[9]['name'],
            'age':request.json[9]['age'],
            'city':request.json[9]['city'],
            'games':request.json[9]['games'],
            'achievements':request.json[9]['achievements'],
            'followers':request.json[9]['followers']
                }

        ]).inserted_ids)

        results = []

        for _id in _ids:
            results.append(str(_id))

        return jsonify({'inserted_ids':results})

    def delete(self):
        return database.db.Badge.delete_many({}).deleted_count
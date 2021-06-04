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

    def delete(self):
        return database.db.Badge.delete_many({}).deleted_count
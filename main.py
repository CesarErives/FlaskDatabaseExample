from flask import Flask, app, json, jsonify,request
from flask.wrappers import Response
from flask_restful import Api,Resource,reqparse,abort
from flask_pymongo import pymongo
from bson.json_util import dumps,ObjectId
import db_config as database

#Resources
from res.badge import Badge


app=Flask(__name__)
api=Api(app)

api.add_resource(Badge,'/new/','/<string:by>=<string:data>/')
api.add_resource(Test,'/test/')


if __name__ == '__main__':
    app.run(load_dotenv=True)
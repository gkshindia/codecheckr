import os
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


class UsersPing(Resource):

    def get(self):
        return {
            "status": "success",
            "message": "ping pong"
        }


api.add_resource(UsersPing, '/users/ping')

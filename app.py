# Import libraries
import os

from flask import Flask, redirect, render_template, session, url_for, send_from_directory
from flask_socketio import SocketIO, emit, join_room
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #   comment this on deployment
from api.HelloApiHandler import HelloApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) # comment this on deployment
api = Api(app)

@app.route("/", defaults={'path' : ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')
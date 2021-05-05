from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from random import seed
import random
import string

from mongodb import User

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET' :
      user = User({"_id":id})
      if user.reload() :
         return user
      else :
         return jsonify({"error": "User not found"}), 404
   elif request.method == 'DELETE' :
      deleteUser = User({"_id":id})
      resp = deleteUser.remove() 
      if resp['n'] == 1 :
         return jsonify({}), 204
      else :
         return jsonify({"error": "User not found"}), 404
   

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job :
         users = User().find_by_name_and_job(search_username, search_job)
      elif search_username :
         users = User().find_by_name(search_username)
      elif search_job :
         users = User().find_by_job(search_job)
      else :
         users = User().find_all()
      return {"users_list" : users}
   elif request.method == 'POST':
      userToAdd = request.get_json()
      newUser = User(userToAdd)
      newUser.save()
      resp = jsonify(newUser), 201
      return resp
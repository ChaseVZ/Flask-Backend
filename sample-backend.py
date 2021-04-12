from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from random import seed
import random
import string


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/<id>', methods=['DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           if request.method == 'DELETE' : 
              users['users_list'].remove(user)
              resp = jsonify(success=True)
              if resp.status_code == 200:
                 resp.status_code = 204
              return resp 
           return user
      return ({})
   return users

def find_users_by_name(name):
   subdict = {'users_list' : []}
   for user in users['users_list']:
      if user['name'] == name:
         subdict['users_list'].append(user)
   return subdict  

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      elif search_username  :
         return find_users_by_name(search_username)  
      elif search_job  :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      # seed(74582)[]
      userToAdd = request.get_json()
      id = str(random.choice(string.ascii_letters))
      id = id + str(random.randint(1,999))
      id = id.lower()
      userToAdd['id'] = id
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      if resp.status_code == 200 :
         resp.status_code = 201
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      userToDelete = request.get_json()
      users['users_list'].remove(userToDelete)
      resp2 = jsonify(success=True)
      if resp.status_code == 200:
         resp.status_code = 204
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp2



# @app.route('/users')
# def get_users():
#    search_username = request.args.get('name') #accessing the value of parameter 'name'
#    if search_username :
#       subdict = {'users_list' : []}
#       for user in users['users_list']:
#          if user['name'] == search_username:
#             subdict['users_list'].append(user)
#       return subdict
#    return users

users = { 
    'users_list' :
    [
    { 
        'id' : 'xyz789',
        'name' : 'Charlie',
        'job': 'Janitor',
    },
    {
        'id' : 'abc123', 
        'name': 'Mac',
        'job': 'Bouncer',
    },
    {
        'id' : 'ppp222', 
        'name': 'Mac',
        'job': 'Professor',
    }, 
    {
        'id' : 'yat999', 
        'name': 'Dee',
        'job': 'Aspring actress',
    },
    {
        'id' : 'zap555', 
        'name': 'Dennis',
        'job': 'Bartender',
    }
    ]
}
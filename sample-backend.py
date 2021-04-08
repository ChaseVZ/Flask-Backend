from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

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

@app.route('/users/<job>')
def get_user(job):
   if job :
      for user in users['users_list']:
        if user['job'] == job:
           return user
      return ({})
   return users

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      userToDelete = request.get_json()
      users['users_list'].remove(userToDelete)
      resp2 = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp2

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
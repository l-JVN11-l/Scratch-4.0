from flask import Flask, render_template
import functions as f
import requests 


app = Flask(__name__)


@app.route('/')
def showWelcomePage():
  return render_template(
    'index.html'
  )
  # ^ this is how the home page functions, when a user is defined it will show the user page instead

@app.route('/users/<user>')
def index(user):
  print (user)
  username = user
  yn = ''
  status = ''
  userInfo = ''

  if f.user_found(username):
    yn = True
    status = f.scratcher(username)
    userInfo = f.get_user_info(username)
  else:
    yn = False

  return render_template(
    'users.html',
    username=username,
    status=status,
    pfpHtml=yn,
    pfpLink=userInfo['pfpLink'],
    userID=userInfo['userId'],
    userBio=userInfo['userBio'],
    userWiwo=userInfo['userWiwo'],
    userJoined=userInfo['userJoined'],
    userScratchTeam=userInfo['userScratchTeam']
  )

app.run(host='0.0.0.0', port=81, debug=True)

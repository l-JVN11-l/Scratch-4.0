from flask import Flask, render_template
import functions as f
import requests 
app = Flask(__name__)

@app.route('/')
def index():
  # false user not found
  username = 'ScratchTheCoder12345'
  yn = None
  status = None

  if f.user_found(username):
    yn = True
    status = f.scratcher(username)
  else:
    yn = False


  return render_template(
    'index.html',
    username=username,
    status=status,
    pfpHtml=yn
  )

app.run(host='0.0.0.0', port=81, debug=True)

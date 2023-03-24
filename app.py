# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect

from model import get_breakfast_rating
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)

# -- Routes section --

# INDEX
@app.route('/')
@app.route('/index')
def index():
  props = {
    "title": "My Breakfast Shouter",
    "first_name":"User"
  }
  return render_template("index.html", time = datetime.now(), props=props)

# RESULTS
@app.route('/results', methods=['GET', 'POST'])
def results():
  if request.method == 'POST':
    print(request.form)
    user_name = request.form["nickname"]
    user_breakfast = request.form["breakfast"]
    breakfast_rating = get_breakfast_rating(user_breakfast)
    return render_template(
      "breakfast.html", 
      user_name=user_name,
      user_breakfast=user_breakfast,
      breakfast_rating=breakfast_rating
    )
  else:
    return redirect('/')
  
# SECRET
@app.route('/secret')
def secret():
  return "<h1>You found the secret!</h1>"
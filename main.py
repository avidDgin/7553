#Main python file
#Sources: https://www.geeksforgeeks.org/convert-mp3-to-wav-using-python/


# import audio.py
from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from os import path
  

# Creating flask app and passing it to bootstrap
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manipulation')
def manip():
    return render_template('manipulation.html')

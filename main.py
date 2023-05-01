#Main python file

# Imports
from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# Creating flask app and passing it to bootstrap
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')



#Main python file

# Imports
from image_info import image_info
from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

filters = ["RGB", "Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

# Creating flask app and passing it to bootstrap
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/imageManip')
def imageManip():
    return render_template('imageManip.html', image_info = image_info, filters = filters)

@app.route('/filter/<image_id>/<selected_filter>')
def filter(image_id, selected_filter):
    for image in image_info:
        if image['id'] == image_id:
            new_image = image

    im = Image.open(f'static/images/{image_id}.jpg')
    im_height = im.height
    im_width = im.width
    im_format = im.format
    im_mode = im.mode

    return render_template('filter.html', image_info = new_image, 
    image_id = image_id, im_height = im_height, im_width = im_width, 
    im_format = im_format, im_mode = im_mode)
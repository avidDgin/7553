#Main python file
#Sources: https://www.geeksforgeeks.org/convert-mp3-to-wav-using-python/

from audio import get_freq
from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from os import path
from image_info import image_info
  
filters = ["Sepia", "Negative", "Grayscale", "Thumbnail"]

def negative_filter(pixel):
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])

def sepia_filter(pixel):
    # tint shadows
    if pixel[0] < 63:
        r,g,b = int(pixel[0] * 1.1), pixel[1], int(pixel[2] * 0.9)
    # tint midtones
    elif pixel[0] > 62 and pixel[0] < 192:
        r,g,b = int(pixel[0] * 1.15), pixel[1], int(pixel[2] * 0.85)
    # tint highlights
    else:
        r = int(pixel[0] * 1.08)
        g,b = pixel[1], int(pixel[2] * 0.5)
    return (r, g, b)

def grayscale_filter(pixel):
    lumi = int( pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114 )
    return (lumi,) * 3

def thumbnail_filter(new_image):
    w, h = new_image.width, new_image.height
    my_trgt = Image.new('RGB',(w, h), 'salmon')

    target_x = 0
    for source_x in range(0, new_image.width, 2):
        target_y = 0
        for source_y in range(0, new_image.height, 2):
            p = new_image.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), p)
            target_y += 1
        target_x += 1
    my_trgt.save(f'static/images/filtered_image.jpg')

# Creating flask app and passing it to bootstrap
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manipulation')
def manip():
    return render_template('manipulation.html')

@app.route('/audio')
def audio():

    #Opening and executing audio file
    with open("audio.py") as f:
        exec(f.read())

    return render_template('audio.html')

@app.route('/imageManip')
def imageManip():
    return render_template('imageManip.html', image_info = image_info)

@app.route('/filter/<image_id>')
def filter(image_id):
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
    im_format = im_format, im_mode = im_mode, filters = filters)

@app.route('/displayImage/<selected_filter>/<image_id>')
def display(selected_filter, image_id):
    if (selected_filter == "Negative"):
        new_image = Image.open(f'static/images/{image_id}.jpg')
        new_list = map(negative_filter, new_image.getdata())
        new_image.putdata(list(new_list))
        new_image.save(f'static/images/filtered_image.jpg')

    if (selected_filter == "Grayscale"):
        new_image = Image.open(f'static/images/{image_id}.jpg')
        new_list = map(grayscale_filter, new_image.getdata())
        new_image.putdata(list(new_list))
        new_image.save(f'static/images/filtered_image.jpg')

    if(selected_filter == "Sepia"):
        new_image = Image.open(f'static/images/{image_id}.jpg')
        new_list = map(sepia_filter, new_image.getdata())
        new_image.putdata(list(new_list))
        new_image.save(f'static/images/filtered_image.jpg')

    if(selected_filter == "Thumbnail"):
        new_image = Image.open(f'static/images/{image_id}.jpg')
        thumbnail_filter(new_image)

    return render_template('display.html')
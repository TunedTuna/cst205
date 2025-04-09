from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5
from idk_dict import wizard_spells
import random
# from PIL import Image

# create an instance of Flask
app = Flask(__name__)
boostrap = Bootstrap5(app)
# route decorator binds a function to a URL
# https://github.com/TunedTuna/cst205/blob/main/lab15_w10_flask1.py
@app.route('/')
def hello():
  return render_template('example_home.html', wizard_spells=wizard_spells)

# @app.route('/templates')
# def t_test():
#   return render_template('random.html',im=rngImg)


@app.route('/templates')
def t_test():
  return render_template('example1.html')


# im1= Image.open('flask_app_x\static\images\gettyimages-157510003-612x612.jpg')
# im2= Image.open('flask_app_x\static\images\image-yellow-reverse-card-uno-hd-png-download-m1v7xrldcsrxuub3.png')
# im3= Image.open('flask_app_x\static\images\Userbox_creeper.svg.png')

# image_list=[im1,im2,im3]
# rngInt= random.randint(0,2)
# rngImg= image_list[rngInt]

# def map_blue(pixel):
#     return (pixel[0],pixel[1],pixel[2]//2)
# new_list= map(map_blue,rngImg.getdata())
# rngImg.putdata(list(new_list))

# def map_green(pixel):
#     return (pixel[0],pixel[1]//2,pixel[2])
# new_list= map(map_green,rngImg.getdata())
# rngImg.putdata(list(new_list))

# rngImg.save()
# task 4: does not work
#the idea was the store 3 images, call random, turn that negative and save, then call that new negative in /random page
# task 5: i added cheatsheet. no idead what its doing
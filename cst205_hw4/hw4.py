from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5
from image_info import image_info
import random
# from PIL import Image

# create an instance of Flask
app = Flask(__name__)
boostrap = Bootstrap5(app)


@app.route('/')
def welcome():
  return render_template('index.html',rng_list=rng_list)
# info needed to pass thru: img id, img name, index to call data?



@app.route('/templates')
def to_detail():
  return render_template('detail.html')

# use image info and throw all id's into a list
# rng 3 numbers and push them into page
# ...how will it update? idk

img_list=[] #holds img ref
rng_list=[] #holds str of img ref id
fin_list=[] #hold: img ref id, img ref name, img ref index?




for data in image_info:
  counter=0
  img_list.append(data['id'])

for item in img_list:
  print(item)

# ---------------------------------------------
for i in range(3):
  rng_num= random.randint(0,len(image_info)-1)
  rng_list.append(img_list[rng_num])
# print("--------------------------------------------")
for item in rng_list:
  print(item)

# ---------------------------------------------
def store_img(temp_img_id,temp_name,temp_index):
  fin_list.append(dict(
    id=temp_img_id,
    name=temp_name,
    index=temp_index
  ))
  
  







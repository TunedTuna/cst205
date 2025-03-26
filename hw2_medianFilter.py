"""
    Daniel Rodas
    cst 205 section 1

"""
from PIL import Image
from glob import glob

# task 1
def my_median(num):
    num.sort()
    length = len(num)
    mid= length//2
    # print(num[mid])
    return num[mid]


# task2
im = Image.open('img_1.png')
im2= Image.open('img_2.png')
im3= Image.open('img_3.png')

width, height = im.size

red_list=[]
green_list=[]
blue_list=[]
alpha_list=[]
rm=0
gm=0
bm=0
am=0


def scanImage(pic,h,w):
    global red_list, green_list, blue_list
    isRGBA = False
    if len(pic.getpixel((1, 1))) == 4:
        isRGBA= True

    red_list=[]
    green_list=[]
    blue_list=[]
    alpha_list=[]
    for y in range(h):
        for x in range(w):
            # if rgb
            if(isRGBA):
                r,g,b,a= pic.getpixel((x,y))
                red_list.append(r)
                green_list.append(g)
                blue_list.append(b)
                alpha_list.append(a)

            else:
                r,g,b= pic.getpixel((x,y))
                red_list.append(r)
                green_list.append(g)
                blue_list.append(b)
                # if rgba

def medianSet():
    # do the 3 my_median

    rm= my_median(red_list)
    gm=my_median(green_list)
    bm=my_median(blue_list)
    new_color= (rm,gm,bm)
    print(new_color)
    return new_color
scanImage(im, height,width)
im_color=medianSet()

scanImage(im2, height,width)
im2_color= medianSet()

scanImage(im3, height,width)
im3_color=medianSet()

def replacePixel(pic,color_color):
    for y in range(height):
        for x in range(width):
            pic.putpixel((x,y),color_color)
    im.show()

replacePixel(im,im_color)



# task 3
# edit this so we reuse the same base to add new layers on
def copy_image(your_image):
   my_src = your_image
   w,h = my_src.width, my_src.height
   my_trgt = Image.new('RGB', (w,h))

   target_x = 0
   for source_x in range(w):
       target_y = 0
       for source_y in range(h):
           p = my_src.getpixel((source_x, source_y))
           my_trgt.putpixel((target_x, target_y), p)
           target_y += 1
       target_x += 1

   
# get all med of all iamges, then place all matching into new img?
img_list = []
def load_images(location, type):
    for image in glob(f'{location}/*.{type}'):
        img_list.append(Image.open(image))

load_images("hw2_task3_img","png")
# directory dictionary thingies?
image_dict= {
    0: (0,0,0,0),
    1: (0, 0, 0,0),
    2: (0, 0, 0,0),
    3: (0, 0, 0,0),
    4: (0, 0, 0,0),
    5: (0, 0, 0,0),
    6: (0, 0, 0,0),
    7: (0, 0, 0,0),
    8: (0, 0, 0,0),
    9: (0, 0, 0,0),
    10: (0, 0, 0,0),
    11: (0, 0, 0,0),
    12: (0, 0, 0,0),

}
img_dict2=[]



width, height= img_list[0].size
print( height, " and", width)
# loop through the 13 of these?
# for i in range(len(image_dict)):
#     scanImage(image_files[i],height,width)
#     # put data in dict
#     image_dict[i]=medianSet()
for i in range(len(img_list)):
    for y in range(height):
        for x in range(width):
            scanImage(img_list[i],y,x)
            img_dict2.append(medianSet)

    # scanImage(image_files[i],height,width)
    # image_dict[i]= medianSet()

# scanImage(image_files[0],height,width)
# image_dict[0]=medianSet
# print(image_dict)

image = Image.new("RGBA", (width, height))
i=0
image = Image.new("RGBA", (width, height))
# for y in range(height):
#     for x in range(width):
#         im2.putpixel((x,y),img_dict2[i] )
#         i+=1
        

image.show()
# make 13 lists of all pixels in the 13 images, then find the median of those?



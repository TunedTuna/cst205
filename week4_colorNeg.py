from PIL import Image
im = Image.open('penguin.jpg')
negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
im.putdata(negative_list)
im.save('negative_penguin.png')

# task 1 took the exisiting colors on the image and inverted them twice.

# task 2

im2 = Image.open('blueSky.jpg')

def map_blue(pixel):
    return (pixel[0],pixel[1],pixel[2]//2)
new_list= map(map_blue,im2.getdata())
im2.putdata(list(new_list))

def map_green(pixel):
    return (pixel[0],pixel[1]//2,pixel[2])
new_list= map(map_green,im2.getdata())
im2.putdata(list(new_list))

# def map_red(pixel):
#    return (pixel[0]*2, pixel[1], pixel[2])
# new_list = map(map_red, im2.getdata())

im2.show()

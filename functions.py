'''
    Daniel Rodas
    CST 205 Multimedia Design
    3/14/25
    this is the logic of hw 3?
    'back end'
'''
from PIL import Image
from __feature__ import snake_case, true_property
from image_info import image_info
global_url =''

def my_search(input):
    '''
    loop though the image_info
    variable for
        x times input match in a block (title n tags)
        the id of that block to be retuned
    
    '''
    
    slot=0
    temp= -1
    topDog =0 #prev most match
    counter=0 #current iteration
    # 10 items, so loop x10?

    for data in image_info:
        counter=0 #rest this guy ;_;
        print("title: "+data['title']+'\n')
        # have to do the split thingy for title
        words= data['title'].split()
        for w in words:
            
            if w.lower() == input.lower():
                print("title part: "+ w.lower())
                counter+=1
        # if data['title'].lower()==input.lower():
        #     counter+=1
        # loop tags?
        for tagList in data['tags']:
            if input.lower() ==tagList.lower():
                print("tag: "+tagList.lower())
                counter+=1
        # update topDog
        if counter>topDog:
            topDog= counter
            temp=slot
            print("The new top dog is: "+ image_info[temp]['title'])
        slot+=1
        
    
    print('\n\n')
    input+=" and cheese"
    words= f"{image_info[0]['title']}"
    # return the image_info directory?
    if temp>-1:
         return image_info[temp]['id']
    else:
        return -1

def set_none(url):
    im= Image.open(url)
    im.show()
    return url

def set_sepia(url):
     # broken

    return url

def set_negative(url):
    im = Image.open(url)
    negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
    im.putdata(negative_list)
    im.show()
    return url

def set_grayscale(url):
    im2 = Image.open(url)

    new_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3
                    for a in im2.getdata() ]

    im2.putdata(new_list)
    im2.show()
    return url

def set_thumbnail(url):
    # broken
    my_src = Image.open(url)
    w, h = my_src.width//2, my_src.height//2
    my_trgt = Image.new('RGB', (w, h))

    target_x = 0
    for source_x in range(0, my_src.width* 1//2, 2):
        target_y = 0
        for source_y in range(0, my_src.height* 1//2, 2):
            p = my_src.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), p) #this gets out of range?
            target_y += 1
        target_x += 1

    my_trgt.show()

    return url

def sepia(p):
   # tint shadows
   if p[0] < 63:
       r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)

   # tint midtones
   elif p[0] > 62 and p[0] < 192:
       r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)

   # tint highlights
   else:
       r = int(p[0] * 1.08)
       g,b = p[1], int(p[2] * 0.5)

   return r, g, b
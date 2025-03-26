from PIL import Image

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy

from colorthief import ColorThief

# copy_image("w5_img/mountainous-floral-beauty-stockcake.jpg")
base= Image.new('RGB', (750,750),'salmon')

# add 3rd paramter for locttion of print?
# og 100 n 100
def dupe_image(your_img, base_img, daX, daY):
    my_src= Image.open(your_img)

    # new_w, new_h = my_src.width + 200, my_src.height + 200
    my_trgt = base_img

    target_x = daX
    for source_x in range(my_src.width):
        target_y = daY
        for source_y in range(my_src.height):
            pixel = my_src.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), pixel)
            target_y += 1
        target_x += 1
        
    my_trgt.show()
    return my_trgt

dupe_image("w5_img/mountainous-floral-beauty-stockcake.jpg",base,0,0)
dupe_image("w5_img/vibrant-rainbow-landscape-stockcake.jpg",base,300,0)
collage= dupe_image("w5_img/winter-sunset-glow-stockcake.jpg",base,0,400)

# task 3?



# def patch_asscalar(a):
#   return a.item()
# setattr(numpy, "asscalar", patch_asscalar)

# color1_rgb = sRGBColor(255, 0, 0, True)
# color2_rgb = sRGBColor(0, 0, 255, True)

# color1_lab = convert_color(color1_rgb, LabColor)
# color2_lab = convert_color(color2_rgb, LabColor)

# delta_e = delta_e_cie2000(color1_lab, color2_lab)

# print(f'The difference is {delta_e}.')

collage_path = "w5_img/collage_temp.jpg"
collage.save(collage_path)

color_thief= ColorThief(collage_path)
dominant_color=color_thief.get_color(quality=1)

def color_distance(c1, c2):
    r_diff = (c1[0] - c2[0])**2
    g_diff = (c1[1] - c2[1])**2
    b_diff = (c1[2] - c2[2])**2
    return (r_diff + g_diff + b_diff)**(1/2)


def chromakey(src, bg, refp):
   for x in range(src.width):
       for y in range(src.height):
           cur_pixel = src.getpixel((x,y))

           if color_distance(cur_pixel, refp) < 150:
               src.putpixel((x,y), bg.getpixel((x,y)))
      
   return src

bgImg= Image.open("w5_img/pexels-fotios-photos-1107717.jpg")
chromakey(collage,bgImg ,dominant_color)

print("dominant color:", dominant_color)
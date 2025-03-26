from PIL import Image
from colorthief import ColorThief
# t4 imports?
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy
# task 1
im2 = Image.open('rainbow.jpg')

new_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3
                   for a in im2.getdata() ]

im2.putdata(new_list)
im2.show()


#task 2

new_list = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000,) * 3
                                      for a in im2.getdata()]
                                    
im2.putdata(new_list)
im2.show()

# task 3

color_theif= ColorThief('rainbow.jpg')
dominant_color=color_theif.get_color(quality=1)
print("dominant color:", dominant_color)

# task 4
def patch_asscalar(a):
    return a.item()
setattr(numpy,"asscalar",patch_asscalar)

color1_rgb = sRGBColor(255, 0, 0, True)
color2_rgb = sRGBColor(0, 0, 255, True)

color1_lab = convert_color(color1_rgb, LabColor)
color2_lab = convert_color(color2_rgb, LabColor)

delta_e = delta_e_cie2000(color1_lab, color2_lab)

print(f'The difference is {delta_e}.')
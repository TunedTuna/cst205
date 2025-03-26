from PIL import Image
import pickle
x=2
y=3
im= Image.new('RGB',(x,y), color=(255,255,255))
# task 1?
print(im.size)

# [
#   [(54,54,54), (204,82,122), (71,71,71)]
#   [(232,22,93) (54,54,54), (168,167,167)]
# ]
color_palette_left= {
    0: (54,54,54),
    1: (204,82,122),
    2: (71,71,71),
}
color_palette_right={
    0: (232,22,93),
    1: (54,54,54),
    2:(168,167,167)
}
im.putpixel((1,0),(255,0,0))
height= 3
width=2
temp=0
for y in range(height): #3 down
    for x in range(width):  #2 across
        if x==0:
            im.putpixel((x,y),color_palette_left[y])
        else:
            im.putpixel((x,y),color_palette_right[y])
im.show()

# task 2

w2=17
h2=28
word_list=[]
line_list=[]
int_list=[]
ww=0
with open ('lisa.txt','r') as my_file:
    line_list= my_file.readlines()

for counter, word_list in enumerate(line_list):
    word_list.split()
    ww +=len(word_list.split())
    # 18= y
    for word in word_list.split():
            int_list.append(int(word))




# for el in word_list.split():
#     int_list.append(int(el))


i=0
im2= Image.new('L',(w2,h2))
for y in range(h2):
    for x in range(w2):
        print(x,y)
        im2.putpixel((x,y),int_list[i] )
        i+=1
        

print(f"what: {ww}")
print(f"int_list size: {len(int_list)}")
print(int_list)
im2.show()



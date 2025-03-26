vermilion =(227,66,52)

if (vermilion[0]> vermilion[1]) and (vermilion[0]>vermilion[2] ):
    print('The color is redish')
elif (vermilion[1]> vermilion[0]) and (vermilion[1]>vermilion[2] ):
    print('The color is bluish')
elif (vermilion[2]> vermilion[0]) and (vermilion[2]>vermilion[1] ):
    print('The color is greenish')


color_list= [ (205, 96, 144) , (28, 134, 238),(72, 209, 204),  (237, 145, 33),
             (250, 250, 70), (245, 50, 245),(100, 231, 231)]
numX=4
# greatest color
if color_list[numX][0] >color_list[numX][1] and color_list[numX][0]>color_list[numX][2]:
    print('The color is redish')
elif color_list[numX][1] >color_list[numX][0] and color_list[numX][1]>color_list[numX][2]:
     print('The color is bluish')
elif color_list[numX][2] >color_list[numX][0] and color_list[numX][2]>color_list[numX][1]:
    print('The color is greenish')
print('\n')

# matching color
if color_list[numX][0] == color_list[numX][1]:
    # red n green
    print("The color is a shade of cyan.")
elif color_list[numX][1] == color_list[numX][2]:
    # green n blue
    print("The color is a shade of magenta")
elif color_list[numX][0] == color_list[numX][2]:
    # red n green
    print("The color is a shade of yellow")
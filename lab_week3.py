# task 1
color_dictionary = {
    'green': [0,256,0],
    'blue':[0,0,256],
    'magenta':[253,61,181]
}

# task 2
print(f"The color green has the red channel {color_dictionary['green'][0]}.")

# task 3
print("\n")
tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141,125,83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35,22,19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}

print(f"the red channel of CLay Creek is {tineye_sample['result'][0]['color'][0]}\n")
print(f"the bluechannel of Seal Brown is {tineye_sample['result'][1]['color'][2]}\n\n")

# task 4
red = 0
blue=0
green =0
rgb_dict = {
    'red':0,
    'green':0,
    'blue':0
}

print("Enter ")
rgb_dict["red"]=int(input ("Enter red : \n"))
rgb_dict["blue"]=int(input ("Enter blue: \n"))
rgb_dict["green"]=int(input ("Enter green: \n"))

print(f"Thank you, your RGB color is ({rgb_dict['red']},{rgb_dict['green']},{rgb_dict['blue']}) \n\n")

# task5
print(f"The r channel is: {rgb_dict['red']}")
print(f"The g channel is: {rgb_dict['green']}")
print(f"The b channel is: {rgb_dict['blue']}\n\n")

# task 6
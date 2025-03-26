from PIL import Image,ImageQt
# the definition of the Pillow image class is on line 533

"""
task 2!
This class represents an image object.  To create
:py:class:`~PIL.Image.Image` objects, use the appropriate factory
functions.  There's hardly ever any reason to call the Image constructor
directly.

* :py:func:`~PIL.Image.open`
* :py:func:`~PIL.Image.new`
* :py:func:`~PIL.Image.frombytes`
"""

# print(dir(ImageQt))
# print("\n")


# make a class object of music

class MySong:
    ''' a class that holds song info  '''
    def __init__(self,name,artist,genre,length,album):
        self.name=name
        self.artist=artist
        self.genre=genre
        self.length=length
        self.album=album
       
    def __str__(self):
        return self.name
    
    def __eq__(self,other):
        if isinstance(self,other):
            return(self.name == other.name)
        return False
    
class SongSnippet(MySong):
    def __init__(self, name, artist, genre, length, album, chorus):
        super().__init__(name, artist, genre, length, album)
        self.chorus=chorus


a=MySong("All Star","Smash Mouth", "Pop?",400,"Shrek")

b=MySong("A Place for My Head","Linkin Park","Rock", 350,"Hybrid Theory")

c=MySong("Disconnected","Pegboar Nerds","Electronic", 2000, "Monstercat004")

d= SongSnippet("Generic Title","Generic Artist","All genres",300,"Generic Album","WEEEEEEEEEEEEEE")

# print(dir(a))
# print (a.name)

# lab 10 

print(a.name)
print (a.name == b.name)

# task3? 
print (d.name)
print (d.name == a.name)
print (a.name == a.name)

# task 4: MyWidget inherits from Qwidget
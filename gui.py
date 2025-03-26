'''
    Daniel Rodas
    CST 205 Multimedia Design
    3/14/25
    this is the gui of hw 3?
    'front end'
'''
import sys


from PIL import Image
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot, Qt


from __feature__ import snake_case, true_property
from image_info import image_info
from functions import my_search,  set_none,set_sepia,set_negative,set_grayscale, set_thumbnail

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # combo box will call repsective method
        self.my_list = ["None","Sepia","Negative","Grayscale","Thumbnail"]
        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)

        vbox = QVBoxLayout()
        self.my_le = QLineEdit("Search an Image!")
        self.my_le.minimum_width = 250
        self.my_le.select_all()
        my_btn = QPushButton("Submit")
        self.my_lbl = QLabel('')
        my_btn.clicked.connect(self.on_submit)
        self.my_le.returnPressed.connect(self.on_submit)
        vbox.add_widget(self.my_le)
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(my_btn)
        vbox.add_widget(self.my_lbl)
        self.set_layout(vbox)

    @Slot()
    def on_submit(self):
        your_song = self.my_le.text
        url= my_search(your_song)
        img= f'hw3_images/{url}.jpg'

        if url ==-1:
            self.my_lbl.text = "error..."
            set_none("hw3_images/no_results.jpg")
        else:
            my_index = self.my_combo_box.current_index
            url= my_search(your_song)
            # self.my_lbl.text = f'Your favorite song is {your_song}'
            # self.my_lbl.text = f'Your favorite song is {my_search(your_song)}'
            
            if my_index ==0:
                set_none(img)
            elif my_index ==1:
                set_sepia(img)
            elif my_index ==2:
                set_negative(img)
            elif my_index ==3:
                set_grayscale(img)
            elif my_index ==4:
                set_thumbnail(img)
            
            


app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(app.exec())
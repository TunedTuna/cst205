import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox)
from PySide6.QtCore import Slot  
from __feature__ import snake_case, true_property

# app = QApplication([])

# # task 1
class ButtonOne(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        my_btn = QPushButton('button 1')
        my_btn2 = QPushButton('button 2')

        self.my_lbl = QLabel('button not yet clicked')

        my_btn.clicked.connect(self.on_click)
        my_btn2.clicked.connect(self.on_click2)

        vbox.add_widget(self.my_lbl)
        vbox.add_widget(my_btn)
        vbox.add_widget(my_btn2)

        self.set_layout(vbox)
        self.resize(400, 400)
        self.show()

    @Slot()
    def on_click(self):
        
        self.my_lbl.text = 'button 1 has been clicked!'
    @Slot()
    def on_click2(self):
        self.my_lbl.text = 'button 2 has been clicked!'

# task 2
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_label1 =  QLabel('CST 205 Color Exchange')
        self.my_list = ["Pick a value", "green", "red", "blue"]
        

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")
        self.rgb_laber= QLabel("RGB: ")
        self.hex_laber= QLabel("Hex: ")


        vbox = QVBoxLayout()
        vbox.add_widget(self.my_label1)
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)
        vbox.add_widget(self.rgb_laber)
        vbox.add_widget(self.hex_laber)

        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

    @Slot()
    def update_ui(self):
        my_text = self.my_combo_box.current_text
        my_index = self.my_combo_box.current_index
        self.my_label.text = f'You chose {self.my_list[my_index]}.'
        # self.rgb_laber.text= f'RGB: {self.my_list[my_index]}'
        # self.hex_laber.text= f'Hex: {self.my_list[my_index]}'
        #                                              green                 
        self.rgb_laber.text= f'RGB: {color_dictionary[self.my_list[my_index]][0]['RGB']}'
        self.hex_laber.text= f'Hex: {color_dictionary[self.my_list[my_index]][0]['HEX']}'
       
        # rgb ???   hex#???
color_dictionary = {
    "green": [
        {
            'RGB':(0,256,0),
            'HEX':'#00ff00',
        },
    ],
    "blue": [
        {
            'RGB':(0,0,256),
            'HEX':'#0000ff',
        },
    ],
    "red": [
        {
            'RGB':(253,61,181),
            'HEX':'#fd3db5',
        },
    ],
}

app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(app.exec())
        


btn_win = ButtonOne()
sys.exit(app.exec())
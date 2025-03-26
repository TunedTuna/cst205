import sys

# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton)
from PySide6.QtCore import Slot  
from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])
layout = QVBoxLayout()

class MyWindow(QWidget):
  def __init__(self):
      super().__init__()

      self.show()

class LayoutOne(QWidget):
   def __init__(self):
      super().__init__()
      label1 = QLabel('Label 1')
      vbox= QVBoxLayout()
      vbox.add_widget(label1)
      self.set_layout(vbox)
      self.resize(800, 600)
      self.show()

class ButtonOne(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()
      my_btn = QPushButton('button 1')
      self.my_lbl = QLabel('button not yet clicked')
      my_btn.clicked.connect(self.on_click)
      vbox.add_widget(self.my_lbl)
      vbox.add_widget(my_btn)
      self.set_layout(vbox)
      self.resize(400, 400)
      self.show()

  @Slot()
  def on_click(self):
      self.my_lbl.text = 'button has been clicked!'

# create a MyWindow object
my_win = MyWindow()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())
# lab11 pt1 task2:
# class QColorDialog- The QColorDialog class provides a dialog widget for specifying colors.

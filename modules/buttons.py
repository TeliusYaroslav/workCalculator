from PyQt5.QtWidgets import QPushButton
from modules.lists import (
        list_numButtons, 
        list_Symbols_Button, 
        list_symbols, 
        list_all_button
    )
from modules.settings_button import *
from modules.windows import win_width, win_height
#
for button in range(10):
    list_numButtons.append(QPushButton(str(button)))
#
for button in list_symbols:
    list_Symbols_Button.append(QPushButton(button))
#
def add_buttons():
    #
    list_button = list()
    #
    for button in list_Symbols_Button:
        #
        if len(list_button) < 4:
            list_button.append(button)
    #
    list_all_button.append(list_button)
    #
    list_button = list()
    index = 7
    #
    for el in range(4,7):
        #
        for num in range(3):
            #
            list_button.append(list_numButtons[index])
            index += 1
        #
        list_button.append(list_Symbols_Button[el])
        #
        list_all_button.append(list_button)
        #
        list_button = list()
        index -= 6

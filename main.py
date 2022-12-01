from window_capture import WindowCapture
import pyautogui
# from functions import random_break

# ONLY USED TO CONFIGURE OFFSETS, NOT TO RUN SCRIPT.

#random_break(2, 3)
print("asd")
# Configuration
client_top_border = 30
client_side_border = 50
offset_minimap_x = 0
offset_minimap_y = 0
offset_run_x = 0
offset_run_y = 0

# window = WindowCapture(client_top_border, client_side_border, offset_minimap_x, offset_minimap_y)
window = WindowCapture()

box = window.get_window('RuneLite - nickname')
coords = window.get_center_minimap(box)
print("coordit tulee")
print(coords)
muspos = pyautogui.displayMousePosition()
print(muspos)
#pyautogui.moveTo(x, y, 2)
#pyautogui.click(coords)
# 712, 140


# TODO: https://github.com/takelley1/OCVBot/blob/c8aa881684168036807e0ec19f2814d85919ac9b/ocvbot/behavior.py#L647
# TODO:
import random

from functions import Image_count, Working_Image_count, climb_up, climb_down
from functions import image_Rec_clicker
from functions import pick_item
from functions import find_Object
from functions import random_break
from functions import Image_color
from functions import release_drop_item
from functions import drop_item
from functions import screen_Image
from functions import random_inventory
from core import findWindow_runelite
import datetime
import pyautogui
import time

findWindow_runelite('nickname')


def get_fish():
    while True:
        fishing = Working_Image_count('fishing_green.PNG')
        if fishing == 1:
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "We are fishing")
            random_break(30, 45)
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "get fish alkaa")
            invent = Image_count('fish_icon_shrimps.png')
            print(now.strftime('%H:%M:%S') + " " + "kalaa invissä: ", + invent)
            find_Object(2)  # amber @ find_Object
            random_break(10, 15)
            print(now.strftime('%H:%M:%S') + " " + "random break loppu")
            invent = Image_count('fish_icon_shrimps.png')
            if invent > 26:
                # invent = Image_count('fish_icon_shrimps.png')
                print("go_tobank 1")
                goto_bank()  # empty_inventory()
        else:
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "we are NOT fishing")
            print(now.strftime('%H:%M:%S') + " " + "get fish alkaa")
            invent = Image_count('fish_icon_shrimps.png')
            print(now.strftime('%H:%M:%S') + " " + "kalaa invissä: ", + invent)
            find_Object(2)  # amber @ find_Object
            random_break(10, 15)
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "random break loppu")
            invent = Image_count('fish_icon_shrimps.png')
            if invent > 26:
                # invent = Image_count('fish_icon_shrimps.png')
                print("go_tobank 2")
                goto_bank()


def empty_inventory():
    now = datetime.datetime.now()
    invent = Image_count('fish_icon_shrimps.png')
    print(now.strftime('%H:%M:%S') + " " + "empty_inv alkaa")
    while invent > 0:
        now = datetime.datetime.now()
        print(now.strftime('%H:%M:%S') + " " + "seur: drop_item")
        drop_item()
        print(now.strftime('%H:%M:%S') + " " + "seur: imagerec_clicker")
        image_Rec_clicker('fish_icon_shrimps.png', 'item', 5, 5, 0.9, 'left')
        print(now.strftime('%H:%M:%S') + " " + "seur: release_drop_item")
        release_drop_item()
        print(now.strftime('%H:%M:%S') + " " + "empty_ivn loppu")
        invent = Image_count('fish_icon_shrimps.png')
        if invent == 0:
            get_fish()


def goto_bank():
    a = random.uniform(0.1, 0.4)
    g = random.uniform(0.1, 0.4)
    k = random.uniform(0.1, 0.4)
    m = random.uniform(0.1, 0.4)
    n = random.uniform(0.1, 0.4)
    o = random.uniform(0.1, 0.4)
    p = random.uniform(0.1, 0.4)
    q = random.uniform(0.1, 0.4)
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "Lets bank stuff")
    pyautogui.moveTo(773, 47, duration=g)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "5sec wait -1-")
    time.sleep(5)
    pyautogui.moveTo(780, 45, duration=k)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "5sec wait -2-")
    time.sleep(5)
    pyautogui.moveTo(797, 57, duration=a)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -3-")
    time.sleep(8)
    pyautogui.moveTo(749, 53, duration=m)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -4-")
    time.sleep(8)
    pyautogui.moveTo(751, 46, duration=o)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -5-")
    time.sleep(8)
    pyautogui.moveTo(718, 142, duration=p)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -6-")
    time.sleep(8)
    pyautogui.moveTo(744, 120, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -7-")
    time.sleep(8)
    pyautogui.moveTo(330, 457, duration=p)
    pyautogui.click()
    print(now.strftime('%H:%M:%S') + " " + "3sec wait - portaat -8-")
    time.sleep(3)
    pyautogui.moveTo(385, 502, duration=p)
    pyautogui.click()
    print(now.strftime('%H:%M:%S') + " " + "1sec wait - portaat2 -9-")
    time.sleep(1)
    climb_up()
    print(now.strftime('%H:%M:%S') + " " + "5sec wait - climb up -10-")
    time.sleep(5)
    pyautogui.moveTo(590, 52, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "7sec wait -11-")
    time.sleep(7)

    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "bank booth click")
    image_Rec_clicker('bankbooth_lumb.png', 'item', 15, 15, 0.9, 'left')
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "pankita shrimps -wait 3 sec")
    time.sleep(3)
    pyautogui.moveTo(738, 517, duration=m)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.moveTo(700, 600, duration=o)
    time.sleep(3)
    pyautogui.click()
    time.sleep(1)
    print(now.strftime('%H:%M:%S') + " " + "Pankitettu shrimpsit")
    pyautogui.moveTo(767, 159, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -12-")
    time.sleep(8)
    pyautogui.moveTo(366, 459, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "2sec wait -13-")
    time.sleep(2)
    pyautogui.moveTo(366, 459, duration=k)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -14-")
    time.sleep(1)
    climb_down()
    time.sleep(2)
    pyautogui.moveTo(840, 75, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -15-")
    time.sleep(8)
    pyautogui.moveTo(839, 148, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -16-")
    time.sleep(8)
    pyautogui.moveTo(815, 176, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -18-")
    time.sleep(8)
    pyautogui.moveTo(777, 186, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -19-")
    time.sleep(8)
    pyautogui.moveTo(769, 155, duration=q)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "8sec wait -20-")
    time.sleep(8)


random_inventory()
get_fish()

goto_bank()

# TODO: https://github.com/takelley1/OCVBot/blob/c8aa881684168036807e0ec19f2814d85919ac9b/ocvbot/behavior.py#L647
# TODO:
import random

from functions import Image_count
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


#def get_wood():


#    j = 0
    #    while j < 10:


#        invent = Image_count('wood_icon1.PNG')
        #        print("Invetoryssä on puuta:")
        #        print(invent)
        #        find_Object(2)
        #        random_break(10, 15)
        #        if invent > 27:
    #            drop_item()
            #            print("drop item")
            #            image_Rec_clicker('wood_icon1.PNG', 'item', 5, 5, 0.9, 'left')
            #            print("image rec clicker")
            #            release_drop_item()
            #            print("release drop item")
#            goto_bank()

#def get_wood():
#    j = 0
#    while j < 10:
#        invent = Image_count('wood_icon1.PNG')
#        print(invent)
#        find_Object(2)
#        random_break(15, 25)
#        if invent > 27:
#           # while invent > 0:
#              drop_item()
#              image_Rec_clicker('wood_icon1.PNG', 'item', 5, 5, 0.9, 'left')
#              release_drop_item()
#              break

# Image_color()


#uustesti
def get_wood():
    while True:
        now = datetime.datetime.now()

        woodcutting = Image_count('woodcutting_green.PNG')
        woodcutting_not = Image_count('woodcutting_green.PNG')
        if woodcutting == 1:
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "We are cutting wood")
            random_break(30, 45)
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "get wood alkaa")
            invent = Image_count('wood_icon1.PNG')
            print(now.strftime('%H:%M:%S') + " " + "Puuta invissä: ", + invent)
            find_Object(2)
            random_break(10, 15)
            print(now.strftime('%H:%M:%S') + " " + "random break loppu")
            invent = Image_count('wood_icon1.PNG')
            if invent > 27:
                invent = Image_count('wood_icon1.PNG')
                print("go_tobank 1")
                goto_bank()
               # empty_inventory()
        else:
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "we are NOT cutting wood")
#            get_wood()
            print(now.strftime('%H:%M:%S') + " " + "get wood alkaa")
            invent = Image_count('wood_icon1.PNG')
            print(now.strftime('%H:%M:%S') + " " + "Puuta invissä: ", + invent)
            find_Object(2)
            random_break(10, 15)
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + " " + "random break loppu")
            invent = Image_count('wood_icon1.PNG')
            if invent > 27:
                invent = Image_count('wood_icon1.PNG')
                print("go_tobank 2")
                goto_bank()
               # empty_inventory()

#        print("get wood alkaa")
#        invent = Image_count('wood_icon1.PNG')
#        print("Puuta invissä: ", + invent)
#        find_Object(2)
#        random_break(10, 15)
#        print("random break loppu")
#        invent = Image_count('wood_icon1.PNG')
#        if invent > 27:
#            invent = Image_count('wood_icon1.PNG')
#            empty_inventory()
# tää on paska
#       if invent < 27:
#           print("false")
#           False
# ei enää paska

def empty_inventory():
    now = datetime.datetime.now()
    invent = Image_count('wood_icon1.PNG')
    print(now.strftime('%H:%M:%S') + " " + "empty_inv alkaa")
    while invent > 0:
        now = datetime.datetime.now()
        print(now.strftime('%H:%M:%S') + " " + "seur: drop_item")
        drop_item()
        print(now.strftime('%H:%M:%S') + " " + "seur: imagerec_clicker")
        image_Rec_clicker('wood_icon1.PNG', 'item', 5, 5, 0.9, 'left')
        print(now.strftime('%H:%M:%S') + " " + "seur: release_drop_item")
        release_drop_item()
        print(now.strftime('%H:%M:%S') + " " + "empty_ivn loppu")
        invent = Image_count('wood_icon1.PNG')
        if invent == 0:
            get_wood()


def goto_bank():
    g = random.uniform(0.1, 0.4)
    k = random.uniform(0.1, 0.4)
    l = random.uniform(0.1, 0.4)
    m = random.uniform(0.1, 0.4)
    n = random.uniform(0.1, 0.4)
    o = random.uniform(0.1, 0.4)
    p = random.uniform(0.1, 0.4)
    q = random.uniform(0.1, 0.4)
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "Lets bank stuff")
    pyautogui.moveTo(751, 71, duration=g)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "5sec wait -1-")
    time.sleep(5)
    pyautogui.moveTo(740, 101, duration=k)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "5sec wait -2-")
    time.sleep(5)
    pyautogui.moveTo(730, 145, duration=l)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "7sec wait -3-")
    time.sleep(7)
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "bank booth click")
    image_Rec_clicker('bankbooth.png', 'item', 20, 20, 0.9, 'left')
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "3sec wait -4-")
    time.sleep(3)
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "Bank all")
    pyautogui.moveTo(506, 635, duration=m)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "Pankitettu")
    print(now.strftime('%H:%M:%S') + " " + "3sec wait -5-")
    time.sleep(3)
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "Mennään takas puiden luo")
    pyautogui.moveTo(815, 78, duration=n)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "7sec wait -6-")
    time.sleep(7)
    pyautogui.moveTo(845, 112, duration=o)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "7sec wait -7-")
    time.sleep(7)
    pyautogui.moveTo(797, 165, duration=p)
    pyautogui.click()
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "7sec wait -8-")
    time.sleep(7)
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S') + " " + "Takas puunhakkuun")


random_inventory()

#testi
#get_wood()
#empty_inventory()
#testi end

#j = 0
#while j < 10:
#    while True:
#        invent = Image_count('wood_icon1.PNG')
#        while invent < 28:
#            invent = Image_count('wood_icon1.PNG')
#            print("get wood cuz inv empty")
#            get_wood()
#            if invent < 27:
#                print("false")
#                False
#        else:
#            print("inv is not empty")
#            empty_inventory()

get_wood()




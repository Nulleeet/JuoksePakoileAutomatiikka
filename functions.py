import numpy as np
import cv2
import pyautogui
import random
import time
from PIL import Image

# pathfinding imports
import pathlib
import random as rand
import pyautogui as pag


def screen_Image(left=0, top=0, right=0, bottom=0):
    myScreenshot = pyautogui.screenshot(region=(0, 0, 865, 830))
    myScreenshot.save("screenshot.png")
    if left != 0 and top != 0 and right != 0 and bottom != 0:
        png = 'screenshot.png'
        im = Image.open(png)  # Käyttää PIL kirjastoa aukasemaan kuvan muistiin
        im = im.crop((left, top, right, bottom))  # croppi pisteet
        im.save('screenshot.png')  # Tallentaa uuden cropatun kuvan


def Image_color():
    screen_Image()
    image = cv2.imread('screenshot.png')
    # Määritä lista rajoista
    empty = ([200, 0, 130], [255, 20, 172])
    empty2 = ([0, 200, 200], [60, 255, 255])
    empty3 = ([15, 20, 40], [25, 40, 78])
    empty4 = ([130, 140, 145], [150, 160, 165])

    boundaries = [
        empty, empty2, empty3, empty4
    ]

    # looppaa yli rajojen
    for (lower, upper) in boundaries:
        # Tee NumPy joukko rajoista
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # etsi värit tietyistä rajoista ja käytä
        # maski
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        # näytä kuvat
        cv2.imshow("images", np.hstack([image, output]))
        cv2.waitKey(0)


def find_Object(item):
    screen_Image()
    image = cv2.imread('screenshot.png')

    # määritä lista boundariesta
    # B,G,R
    red = ([0, 0, 180], [80, 80, 255])  # 0 index
    green = ([0, 180, 0], [80, 255, 80])  # 1 index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 index
    attack_blue = ([250, 250, 0], [255, 255, 5])  # 4 index
    fish = ([0, 200, 200], [0, 178, 178])  # 5 index
    object_list = [red, green, amber, pickup_high, attack_blue, fish]
    boundaries = [object_list[item]]

    # looppaa rajat
    for (lower, upper) in boundaries:
        # Tee NumPy joukko rajoista
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # etsi värit tietyistä boundariesta ja apply
        # the maski
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        # etsi isoin ääriviivat (c) areasta
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        whalf = max(round(w / 2), 1)
        hhalf = max(round(h / 2), 1)
        # wmin=min(round(whalf/2),0)
        # hmin=min(round(hhalf/2),0)
        x = random.randrange(x + whalf, x + w)  # 950,960
        print('x: ', x)
        y = random.randrange(y + hhalf, y + h)  # 490,500
        print('y: ', y)
        b = random.uniform(0.2, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)


def pick_item(v, u):
    c = random.uniform(0.3, 0.7)
    d = random.uniform(0.05, 0.15)
    x = random.uniform(v - 10, v + 10)
    print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.2, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)


def image_Rec_clicker(image, event, iheight, iwidth, threshold, clicker):
    global icoord
    global iflag
    myScreenshot = pyautogui.screenshot(region=(0, 0, 612, 660))
    myScreenshot.save(r"screenshot.png")
    img_rgb = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    iflag = False
    event = event
    for pt in zip(*loc[::-1]):
        #        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1], + h), (0, 0, 255), 2)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if pt is None:
            iflag = False
        else:
            iflag = True
            x = random.randrange(iwidth, iwidth + 20)
            y = random.randrange(iheight, iheight + 20)
            icoord = pt[0] + iheight + x
            icoord = (icoord, pt[1] + iwidth + y)
            b = random.uniform(0.2, 0.7)
            pyautogui.moveTo(icoord, duration=b)
            b = random.uniform(0.1, 0.3)
            pyautogui.click(icoord, duration=b, button=clicker)
        return iflag


def Image_count(object):
    counter = 0
    myScreenshot = pyautogui.screenshot(region=(661, 482, 865, 830))
    #myScreenshot = pyautogui.screenshot(region=(0, 0, 865, 830))
    myScreenshot.save('screenshot.png')
    img_rgb = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(object, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter

def Working_Image_count(object):
    counter = 0
    myScreenshot = pyautogui.screenshot(region=(0, 0, 865, 830))
    myScreenshot.save('screenshot.png')
    img_rgb = cv2.imread('screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(object, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter


def drop_item():
    pyautogui.keyUp('shift')
    c = random.uniform(0.1, 0.2)
    d = random.uniform(0.2, 0.23)

    time.sleep(c)
    pyautogui.keyDown('shift')
    time.sleep(d)


def release_drop_item():
    e = random.uniform(0.2, 0.3)
    f = random.uniform(0.1, 0.2)

    time.sleep(e)
    pyautogui.keyUp('shift')
    pyautogui.press('shift')
    time.sleep(f)


def random_break(minsec, maxsec):
    e = random.uniform(minsec, maxsec)
    time.sleep(e)

def random_inventory():
    # global newTime_break
    print('inventory tab')
    b = random.uniform(1.5, 15)
    pyautogui.press('f4')
    time.sleep(b)
    pyautogui.press('f4')
    b = random.uniform(1.5, 2)
    time.sleep(b)
    pyautogui.press('esc')
    # newTime_break = True

def climb_up():
    q = random.uniform(0.1, 0.4)
    pyautogui.moveTo(290, 725, duration=q)
    pyautogui.click()

def climb_down():
    q = random.uniform(0.1, 0.4)
    pyautogui.moveTo(280, 760, duration=q)
    pyautogui.click()

"""
Pathfinding alkaa
"""


"""
Pathfinding loppuu
"""

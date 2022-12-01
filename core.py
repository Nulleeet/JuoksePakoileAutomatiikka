import win32gui
global hwnd
hwnd = 0


def findWindow_runelite(Name):
    global hwnd
    hwnd = win32gui.FindWindow(None, "Runelite - " + Name)
    # hwnd = win32gui.GetForegroundWindow()
    print('findWindow:', hwnd)
    win32gui.SetForegroundWindow(hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.SetForegroundWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)


#findWindow_runelite('Nickname')

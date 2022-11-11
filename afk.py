import pyautogui as pag
import win32api
import random
import time
import keyboard

# Root
use_full_res = False
use_win32API_movement = True

# ! Need to hold down the key to stop
while keyboard.is_pressed('q') == False:
    timer = random.uniform(2.0, 5.0)
    if use_full_res:
        x = random.randint(0, win32api.GetSystemMetrics(0))
        y = random.randint(0, win32api.GetSystemMetrics(1))
    else:
        x = random.randint(600,700)
        y = random.randint(200,600)

    if use_win32API_movement:
        win32api.SetCursorPos((x,y))
    else:
        speed = random.uniform(0.5, 1.0)
        pag.moveTo(x,y,speed)
    
    time.sleep(timer)
    
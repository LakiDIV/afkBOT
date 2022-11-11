import pyautogui as pag
import random
import time
import keyboard
import win32api

use_win32API_movement = True

# ! Need to hold down the key to stop
while keyboard.is_pressed('q') == False:
    x = random.randint(600,700)
    y = random.randint(200,600)
    
    timer = random.uniform(2.0, 5.0)
    if use_win32API_movement:
        win32api.SetCursorPos((x,y))
    else:
        speed = random.uniform(0.5, 1.0)
        pag.moveTo(x,y,speed)
    
    time.sleep(timer)
    
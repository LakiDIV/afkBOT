import pyautogui as pag
import win32api
import random
import time
import keyboard

# Root
use_full_res = False
use_win32API_movement = True

break_loop_flag = False

def handle_q_button():
    print('q pressed')
    global break_loop_flag
    break_loop_flag = True

keyboard.add_hotkey('q', handle_q_button)

while True:
    if break_loop_flag:
        break
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
    
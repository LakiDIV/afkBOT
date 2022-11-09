import pyautogui as pag
import random
import time

while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    speed = random.uniform(0.5, 1.0)
    timer = random.uniform(2.0, 5.0)
    pag.moveTo(x,y,speed)
    time.sleep(timer)
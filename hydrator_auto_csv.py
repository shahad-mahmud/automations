import pyautogui as pg
import time

pg.PAUSE = 2.5

start_range = int(input('Enter start point: '))

button_x = 488
button_y = 315

for i in range(start_range, 381):
    # click on data set
    pg.click(192, 100)

    #click on csv button
    pg.click(button_x, button_y)
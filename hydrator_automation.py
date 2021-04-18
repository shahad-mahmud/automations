import pyautogui as pg
import time

start_range = int(input('Enter start point: '))

file_x = 470
file_y = 190

for i in range(start_range, 291, -1):
    print(i)
    # click on the Add button
    pg.click(269, 105)
    time.sleep(1.5)

    # click on 'select tweet ID file' button
    pg.click(182, 289)
    time.sleep(1.5)

    # click on the 'processed_for_ids' folder
    pg.click(165, 407)
    time.sleep(1.5)

    # get to the file
    pg.moveTo(500, 300)
    time.sleep(1.5)
    if i < 310:
        pg.scroll(-24)
        time.sleep(1.5)
        file_y = 360 + 23 * (309 - i)
    elif i < 334:
        pg.scroll(-16)
        time.sleep(1.5)
        file_y = 150 + 23 * (333 - i)
    elif i < 359:
        pg.scroll(-8)
        time.sleep(1.5)
        file_y = 183 + 24 * (358 - i)
    else:
        file_y = 190 + 24 * (382 - i)

    # click on file
    pg.click(file_x, file_y, 1)
    time.sleep(1.5)
    pg.click(file_x, file_y, 2)
    time.sleep(1.5)

    # click on title
    pg.click(152, 493)
    time.sleep(1.5)

    # enter title
    pg.typewrite(str(i))
    time.sleep(1.5)

    # click on 'add dataset' button
    pg.click(156, 733)
    time.sleep(1.5)

    # click on 'datasets' button
    pg.click(186, 105)
    time.sleep(1.5)

    # click on start button
    pg.click(496, 314)
    time.sleep(1.5)

    # click on hydrating folder
    pg.click(165, 408)
    time.sleep(1.5)

    # click on save
    pg.click(1238, 52)
    time.sleep(1.5)

    # sleep for 6 min and pause 
    time.sleep(360)
    pg.click(496, 314)

    # sleep 10 sec and start
    time.sleep(10)
    pg.click(496, 314)

    # sleep for 6 min and start new
    time.sleep(360)


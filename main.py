from pyautogui import moveTo, click
from time import sleep

for _ in range(3):
    rows = 8
    cols = 3

    x_pos = 455 # 160
    y_pos = 630 #50

    moveTo(1, 1)

    for _ in range(rows):
        for _ in range(cols):

            moveTo(x_pos, y_pos)
            click()
            sleep(1)

            x_pos += 160

        x_pos = 455
        y_pos += 48

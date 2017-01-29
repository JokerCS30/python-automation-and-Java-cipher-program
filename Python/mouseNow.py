import pyautogui, time

# mouseNow.py - display the mouse cursers current position

print('press ctrl + c to quit')
pyautogui.click(609, 524)


try:
    while True:
        # get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)



except KeyboardInterrupt:
    print('\nDone')

print(positionStr, end='')
print('\b' * len(positionStr), end='', flush=True)

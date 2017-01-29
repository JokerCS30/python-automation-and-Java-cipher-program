import pyautogui, time, pyperclip

url = pyperclip.paste()


pyautogui.click(609, 524)
time.sleep(0.1)
pyautogui.click(500, 0)   # this worked


import webbrowser, bs4, time, sys, pyperclip, pyautogui
import sys, pyperclip, requests, bs4, re, getopt

pyautogui.click(960, 540, button='right')
pyautogui.click(697, 619)      # click on player
pyautogui.click(710, 660)     # click steam profile
pyautogui.click(735, 231, button='right')     # right click
pyautogui.click(741, 356)    # copy url
first = pyperclip.paste()
pyautogui.click(1907, 16)   # exit page
pyautogui.press('alt', 'tab') # alt tab

time.sleep(0.5)

pyautogui.click(629, 657)    # click on player
pyautogui.click(638, 697)    # click steam profile
pyautogui.click(735, 231, button='right')     # right click
pyautogui.click(741, 356)    # copy url
second = pyperclip.paste()
pyautogui.click(1907, 16)   # exit page
pyautogui.press('alt', 'tab') # alt tab

time.sleep(0.5)

pyautogui.click(629, 695)    # click on player
pyautogui.click(638, 735)    # click steam profile
pyautogui.click(735, 231, button='right')     # right click
pyautogui.click(741, 356)    # copy url
third = pyperclip.paste()
pyautogui.click(1907, 16)   # exit page
pyautogui.press('alt', 'tab') # alt tab

time.sleep(0.5)

pyautogui.click(629, 733)    # click on player
pyautogui.click(638, 773)    # click steam profile
pyautogui.click(735, 231, button='right')     # right click
pyautogui.click(741, 356)    # copy url
fourth = pyperclip.paste()
pyautogui.click(1907, 16)   # exit page
pyautogui.press('alt', 'tab') # alt tab

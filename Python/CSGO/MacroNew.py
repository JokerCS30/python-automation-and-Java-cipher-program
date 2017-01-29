import pyautogui, time, pyperclip
pyautogui.FAILSAFE = True

pyautogui.click(213, 79)
default = 0.1
chat = pyautogui.prompt('y for all chat, u for team chat')

def t(writing):
    pyautogui.click(213, 79)  # click key
    pyautogui.press(chat)   # enter u or y
    pyautogui.click(921, 610)  # click ok
    pyautogui.click(295, 73)  # click wait
    pyautogui.press('enter')
    pyautogui.click(257, 79)  # click text
    pyautogui.typewrite(writing, 0)  # write the
    pyautogui.click(922, 594)
    pyautogui.click(213, 79)  # click key
    pyautogui.press('enter')
    pyautogui.click(921, 610)
    pyautogui.click(295, 73)  # click wait
    pyautogui.press('enter')


while True:
    writing = pyautogui.prompt('enter message')
    t(writing)


import ctypes, pyautogui
from ctypes import wintypes
import time, pyperclip, random
from random import shuffle
import webbrowser, sys, pyperclip, requests, bs4, re, getopt
from datetime import datetime

name = 'User'
chatKey = ''

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

whichKey = pyautogui.prompt('all chat, or team chat?')
if whichKey == 'all':
    chatKey = 0x59
else:
    chatKey = 0x55


def c(writing):
    PressKey(chatKey)
    ReleaseKey(chatKey)
    time.sleep(0.3) # 0.3
    pyautogui.typewrite(writing, 0) # interval = 0
    PressKey(0x0D)
    ReleaseKey(0x0D)
    time.sleep(0.4) # 0.4

def profileGrab():
    url = pyperclip.paste()
    res = requests.get(url)
    res.raise_for_status()
    steamProfile = bs4.BeautifulSoup(res.text, "html.parser")
    name = steamProfile.select('.actual_persona_name')


    idURL = ('https://steamid.io/lookup/' + url)
    resID = requests.get(idURL)
    resID.raise_for_status()
    steamID = bs4.BeautifulSoup(resID.text, "html.parser")
    id = steamID.find_all(id="a")


    PressKey(0xC0)
    ReleaseKey(0xC0)
    time.sleep(0.5)
    pyautogui.typewrite('status')
    PressKey(0x0D)
    ReleaseKey(0x0D)
    status = pyautogui.prompt('copy server info')
    PressKey(0x1B)
    ReleaseKey(0x1B)
    time.sleep(0.1)
    c('Steam name: ' + name[0].getText().strip())
    c('steamID = ' + id[0].getText().strip())
    charArray = list(status.strip())
    text = ''

    c('Server info:')
    for f in charArray:
        text += f
        if(f == '\n'):
            c(text)
            text = ''

    c(text)
    c('Additional info for database')
    c('date, time : ' + str(datetime.now()))
    c('Priority(9)')
    c('Successfully added Record for user ' + name[0].getText().strip() + ' to steamProfiles.sqlite3')



def analyseText():
    text = pyperclip.paste() # may change

    if bool(re.search('no life', text.lower())):
        c('Are you sure you want to imply this?')
        time.sleep(2)
        if (pyautogui.prompt('go ahead with response') == ''):
            c('I have no life?, impossible.')
            c('I used to have no life when I was a teen')
            c('when I was expelled from college')
            c('when I went to boarding school')
            c('and ended up being kicked out of my boarding house')
            c('Until leaving school, working 3 Jobs')
            c('while studying programming and networking')
            c('I could spend my \'no life\' spare time')
            c('proving my no life skill to you within')
            c('the next few days if you\'re so keen?')

    elif bool(re.search(' loser', text.lower())):
        c('The only loser around here is the one without intelligence')
        c('which would imply yourself rather than me.')
        c('Do you wish to play the game in order to')
        c('distinguish the real loser?')
        c('because my game contains no rules nor boundaries')
        c('however far you are willing to go with your')
        c('pathetic insults will consequentially become')
        c('how far I am willing to go')
        c('Do you wish to Continue: Y or N?')


opt = pyautogui.prompt('1: ananlyseText, 2: profileGrab')

if (opt == '1'):
    analyseText()
elif (opt == '2'):
    profileGrab()

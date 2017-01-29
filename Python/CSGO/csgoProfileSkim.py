import ctypes, pyautogui
from ctypes import wintypes
import time, pyperclip
from random import shuffle
import webbrowser, sys, pyperclip, requests, bs4, re, getopt
name = 'User'


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

chatKey = ''

if pyautogui.prompt('all chat or team chat?') == 'all':
	chatKey = 0x59
else:
	chatKey = 0x55

def c(writing):

    PressKey(chatKey)
    ReleaseKey(chatKey)
    time.sleep(0.4)
    pyautogui.typewrite(writing, 0)
    PressKey(0x0D)
    ReleaseKey(0x0D)
    time.sleep(0.3)




def p(one, two):
    pyautogui.click(one, two)
    time.sleep(0.2)





try:
    while True:
        default = 0.1
        #name = pyperclip.paste()
        steamURL = pyperclip.paste()
        #steamURL = pyautogui.prompt('enter steam url')
        hexArray = ['10', '18', '0E', '09', '13', '05', '0A', '16', '14', '02', '0A', '01']



        res = requests.get(steamURL)
        res.raise_for_status()
        userProfile = bs4.BeautifulSoup(res.text, "html.parser")


        resFriends = requests.get(steamURL + '/friends')
        userFriends = bs4.BeautifulSoup(resFriends.text, "html.parser")
        usersName = userFriends.select('.whiteLink')
        elemsFriends = userFriends.select('.friendBlockContent')

        resGames = requests.get(steamURL + '/games/?tab=all')
        userGames = bs4.BeautifulSoup(resGames.text, "html.parser")
        elemGames = userGames.select('.gameListRow')
        #mostPlayed = elemGames[0].getText().strip()

        user = userProfile.select('.actual_persona_name')
        name = user[0].getText().strip()


        def ten():
            for l in range(10):
		c(re.sub("\n.*", "", elemsFriends[l].getText().strip()))

        def all():
            for j in range(len(elemsFriends)):
                c(re.sub("\n.*", "", elemsFriends[j].getText().strip()))

        c('Steam Name: ' + name)
        c('users friends: ')
        all()

        c('TOR torch search engine results for steam user: ' + name)
        c('December 2016 steam database leak. Search results for username: ' + name)
        c('Results = one. please subscribe to our services for the raw data.')
        c('href=\'trz899adafzf900af0.onion\'')

        break

except KeyboardInterrupt:
    print('done')



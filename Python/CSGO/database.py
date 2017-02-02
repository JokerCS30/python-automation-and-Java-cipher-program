import sqlite3
import ctypes, pyautogui
from ctypes import wintypes
import time, pyperclip
from random import shuffle
import webbrowser, sys, requests, bs4, re, getopt
from datetime import datetime

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


# dk if you can have class scope in this, may need to make python class first
steamName = ''
steamURL = ''
steamFriends = ''
gameHours = ''

idArray = []
nameArray = []
urlArray = []
friendArray = []
mapArray = []
hoursArray = []

def profileSkim():
    global steamFriends
    global steamName
    global steamURL
    global map
    global gameHours
    steamURL = pyperclip.paste()

    res = requests.get(steamURL)
    res.raise_for_status()
    userProfile = bs4.BeautifulSoup(res.text, "html.parser")
    user = userProfile.select('.actual_persona_name')
    steamName = user[0].getText().strip()

    resFriends = requests.get(steamURL + '/friends')
    userFriends = bs4.BeautifulSoup(resFriends.text, "html.parser")
    elemsFriends = userFriends.select('.friendBlockContent')

    try:
        timePlayed = userProfile.select('.game_info_details')
        gameHours = timePlayed[0].getText().split(' ', 1)[0].strip()
    except:
        gameHours = 'private'



def infoTeam():
    def copy(two):
        PressKey(0x09)
        time.sleep(0.3)
        pyautogui.click(629, two, button='right')
        pyautogui.click(629, two)
        pyautogui.click(710, two + 38)  # click steam profile

        time.sleep(2.5)
        ReleaseKey(0x09)
        pyautogui.click(637, 231, button='right')  # right click
        pyautogui.click(741, 356)  # copy url
        time.sleep(0.5)
        urlArray.append(pyperclip.paste())
        pyautogui.click(1907, 16)  # exit page
        pyautogui.press('esc')  # escape
        time.sleep(0.5)

    pyautogui.click(960, 540, button='right')

    def top():
        copy(367)
        copy(407)
        copy(440)
        copy(470)
        copy(500)

    def bottom():
        copy(619)
        copy(657)
        copy(695)
        copy(725)
        copy(755)

    if pyautogui.prompt('t or ct?') == 't':
        bottom()
    else:
        top()

    try:

        for x in range(len(urlArray)):
            res = requests.get(urlArray[x])
            res.raise_for_status()
            userProfile = bs4.BeautifulSoup(res.text, "html.parser")
            user = userProfile.select('.actual_persona_name')
            name = user[0].getText().strip()
            nameArray.append(name)

        for z in range(len(urlArray)):
            res = requests.get(urlArray[z])
            res.raise_for_status()
            userProfile = bs4.BeautifulSoup(res.text, "html.parser")
            friends = ''

            resFriends = requests.get(urlArray[z] + '/friends')
            userFriends = bs4.BeautifulSoup(resFriends.text, "html.parser")
            elemsFriends = userFriends.select('.friendBlockContent')

            try:
                hours = userProfile.select('.game_info_details')
                hoursArray.append(hours[0].getText().split(' ', 1)[0].strip())
            except:
                hoursArray.append('private')

            try:
                for j in range(len(elemsFriends)):
                    for k in range(len(nameArray)):
                        if ((re.sub("\n.*", "", elemsFriends[j].getText().strip())) == nameArray[k]):
                            friends += (re.sub("\n.*", "", elemsFriends[j].getText().strip()))
                            friends += '; '
                friendArray.append(friends)

            except:
                print('error')

    except:
        print('error')





def database(name, url, friends, hours):
    sqlite_file = 'csgo.sqlite'
    table_name = 'players'
    field_type = 'TEXT'
    column_name = 'steamName'
    column_url = 'url'
    column_friends = 'friendsLobbied'
    column_map = 'map'
    column_date = 'date'
    column_info = 'info'
    info = pyautogui.prompt('any info on ' + name)


    date = str(datetime.now())

    # connect to database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()


    try:
        c.execute(
            "INSERT INTO players (steamName, url, friendsLobbied, map, date, info, hours) VALUES ('" + name + "', '" + url + "', '" + friends + "', '" + map + "', '" + date + "', '" + info + "', '" + hours + "')")
    except sqlite3.Error as er:
        print ('er:', er)


    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()

map = pyautogui.prompt('what map?')

if (pyautogui.prompt('team or single profile?') == 'team'):
    infoTeam()

    for z in range(len(urlArray)):
        database(nameArray[z], urlArray[z], friendArray[z], hoursArray[z])

else:
    profileSkim()
    print(steamName + steamURL + 'not checked' + gameHours)
    database(steamName, steamURL, 'Not Checked', gameHours)

url = 'http://steamcommunity.com/profiles/76561198346404137/'
import ctypes, pyautogui
from ctypes import wintypes
import time, pyperclip, random
from random import shuffle
import webbrowser, sys, pyperclip, requests, bs4, re, getopt

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





def lobbied():
    urlArray = []

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

    #pyautogui.click(960, 540, button='right')

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

    if pyautogui.prompt('t or ct ?') == 't':
        bottom()
    else:
        top()




    try:

        default = 0.1
        steamURL = pyperclip.paste()

        nameArray = []

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
            usersName = userFriends.select('.whiteLink')
            elemsFriends = userFriends.select('.friendBlockContent')

            user = userProfile.select('.actual_persona_name')
            name = user[0].getText().strip()

            hours = userProfile.select('.game_info_details')




            try:
                for j in range(len(elemsFriends)):
                    for k in range(len(nameArray)):
                        if ((re.sub("\n.*", "", elemsFriends[j].getText().strip())) == nameArray[k]):
                            friends += (re.sub("\n.*", "", elemsFriends[j].getText().strip()))
                            friends += ';  '

            except:
                print(name + '  private')

            try:
                c(name + ' friends in game: ' + friends)
            except:
                print('cant print table')

            print()


    except:
        print ('error')


def profileSkim():
    try:
        while True:
            steamURL = pyperclip.paste()
            amount = pyautogui.prompt('ten or all friends')


            res = requests.get(steamURL)
            res.raise_for_status()
            userProfile = bs4.BeautifulSoup(res.text, "html.parser")
            user = userProfile.select('.actual_persona_name')

            resFriends = requests.get(steamURL + '/friends')
            userFriends = bs4.BeautifulSoup(resFriends.text, "html.parser")
            elemsFriends = userFriends.select('.friendBlockContent')

            name = user[0].getText().strip()

            def ten():
                for l in range(10):
                    c(re.sub("\n.*", "", elemsFriends[l].getText().strip()))


            def all():
                for j in range(len(elemsFriends)):
                    c(re.sub("\n.*", "", elemsFriends[j].getText().strip()))

            c('Steam Name: ' + name)
            c('users friends: ')
            if (amount == 'ten'):
                ten()
            else:
                all()

            c('TOR torch search engine results for steam user: ' + name)
            c('December 2016 steam database leak. Search results for username: ' + name)
            c('Results = one. please subscribe to our services for the raw data.')
            c('href=\'trz899adafzf900af0.onion\'')
            break

    except:
        print('error')

def fakeInfo():
    firstArray = ['Jessica', 'Sheniqua', 'Jacinta', 'Gerald', 'Martin']
    surArray = ['Saprinkal', 'Shkrelli', 'Wallace', 'Mehabhiek', 'Cabello']
    emailArray = ['skuxKidd@transgoths.com', 'skaterG@hi5.com', 'lvl80Wizard@silkroad.com', 'imNotTwelve@raroprimary.school.au', 'tooKewl4u@ministry.gov.au']
    fatherArray = ['Melania', 'none', 'Emerald', 'Sapphire', 'Ahled']
    brotherArray = ['Ivanka', 'Tiffany', 'Harold', 'Britney', 'Sashita']
    sisterArray = ['none', 'Matt', 'Zoey', 'John', 'Marilyn']
    schoolArray = ['St Francines Girls Boarding School', 'st Hoseas Girls public', 'Inuman Elementary School', 'Governor Dummer Academy', 'West Fukasumi Titnipple High']
    ipArray = ['223.240.28.128', '250.252.192.199', '216.32.105.204', '162.85.167.53', '151.54.55.126']



    c('First Name: ' + firstArray[random.randrange(5)] + ', Surname: ' + surArray[random.randrange(5)])
    c('Age: 12, IQ: 2 x Age')
    c('Email address: ' + emailArray[random.randrange(5)])
    c('Mother: none')
    c('Father: ' + fatherArray[random.randrange(5)])
    c('Sisters: ' + sisterArray[random.randrange(5)])
    c('Brothers: ' + brotherArray[random.randrange(5)])
    c('Residency: 13th floor of anything')
    c('School: ' + schoolArray[random.randrange(5)])
    c('IP addr: ' + ipArray[random.randrange(5)])
    c('Now as you can see I have your real info')
    c('please pay 5 btc to wwww.go.kl/asdo12 otherwise ')
    c('I will anonymously riddle you until you cry')
    c('I will have anonymous ddos you while I wear a hoodie')
    c('I will download programs off the darkweb')
    c('using TOR to steal your worm god skin(f.society)')
    c('I will not forget, I will not forbid(CS30)')
    c('I am Norwegian, inject mysql(Mr.Robot Abort)')

def explain():
    c('I don\'t do anything like copy and paste,')
    c('it\'s simply an automation script')
    c('using pythons beautiful soup module')
    c('it webscrapes the html data off the steam url')
    c('based on what element I pass')
    c('for getting your friends names it is')
    c('friends = requests.get(steamURL + \'/friends\')')
    c('userFriends = bs4.BeautifulSoup(friends.text, "html.parser")')
    c('elemsFriends = userFriends.select(\'.friendBlockContent\')')
    c('then for only printing the first ten:')
    c('for x in range(10):')
    c('       looptext(elemsFriends[x].getText().strip())')
    c('I also write a regex to take away the extra info')
    c('in the element of the friend like what game they\'re in')
    c('or last online at blah blah etc')
    c('that only explains a few lines of the script ')
    c('however I could walk you through the whole thing')
    c('if you really want to claim I didn\'t code it ')
    c('check out my github to see my code with proof I wrote it')
    c('https://github.com/ClownPrinceCS30/python-automation-and-Java-cipher-program')

def fakeHacks():
    c('if steamUser.isSalty():')
    c('    autoBuy.Negev')
    c('    hacks(spin, aim, walls).ON')
    c('    user.stealInventory')
    c('    user.stealTheirLollies')
    c('    user.batheInTheirTears')

def fakeIPs():
    urlArray = []

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

        default = 0.1
        steamURL = pyperclip.paste()
        ipArray = ['253.126.205.151', '162.79.118.210', '83.249.150.53', '219.219.90.85', '248.88.176.70']
        nameArray = []

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
            usersName = userFriends.select('.whiteLink')
            elemsFriends = userFriends.select('.friendBlockContent')

            user = userProfile.select('.actual_persona_name')
            name = user[0].getText().strip()



        for j in range(len(nameArray)):
            c(nameArray[j].center(30) + ipArray[j].center(30))





    except:
        print ('error')

def metasploit():
    c('NIC.macchanger -r')
    c('NIC.monitormode')
    c('service mysql start')
    c('msfconsole')
    c('setg RPORT = 5543')
    c('setg RHOST = 152.213.14.154')
    c('use Unix/authenticateUser/auxillary/scanner')
    c('set Threads = 5')
    c('run')
    c('.')
    c('.')
    c('results = ack packets sent to port 8080')
    c('use Unix/TCPserver/handler')
    c('set Threads = 5')
    c('run -vv')
    c('initialising reverse TCP handler')
    c('listening on port 8080 for TCP client')
    c('msfvenom unix/shell_bind_tcp EXITFUNC=seh LPORT=5543')
    c('sending payload through TCP')
    c('.')
    c('.')
    c('.')
    c('connection on port 5543 established')
    c('setting up reverse shell')
    c('killing reverse TCP handler on port 8080; no results')
    c('reverse shell initialised use -h for commands')
    c('-->')
    c('skins = game.Players(inv)')
    c('cd ..')
    c('->')
    c('ls')
    c('. .. backup logs routing serverSource anti-cheat lastLog.txt')
    c('cd routing')
    c('ls')
    c('. .. routingTableLog.txt dhcp.info dns.info')
    c('cat routingTableLog.txt')
    c('salt.salt.salt.salt.salt.salt.salt')

def github():
    c('https://github.com/ClownPrinceCS30/python-automation-and-Java-cipher-program')

def tcp():
    url = pyperclip.paste()
    res = requests.get(url)
    res.raise_for_status()
    userProfile = bs4.BeautifulSoup(res.text, "html.parser")
    user = userProfile.select('.actual_persona_name')
    name = user[0].getText().strip()
    ipArray = ['252.199.3.79', '219.35.58.144', '126.137.6.118', '185.15.157.25', '180.249.184.44', '235.87.171.91', '217.111.7.191', '237.45.100.205', '227.110.186.127', '234.151.1.17']
    ip = ipArray[random.randrange(10)]

    c(name.center(30) + ip)
    c('import socket')
    c('import threading')
    c('bind_ip = ' + '"' + ip + '"')
    c('bind_port = 5543')
    c('server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)')
    c('server.bind((bind_ip, bind_port))')
    c('server.listen(5)')
    c('Listening on (' + ip + ', 5543)')
    c('def handle_client(client_socket):')
    c('request = client_socket.recv(1024)')
    c('client_socket.send(ARP_MITM)')
    c('client_socket.close()')
    c('client, addr = server.accept()')
    c('Accepted connection')
    c('client_handler = threading.Thread(target=handle_client, args=(client,))')
    c('client_handler.start()')

def mrRobot():
    c('If you died, would anyone care?')
    c('Would they really care?')
    c('Maybe, they\'d cry for a day.')
    c('But, let\'s be honest, no one would give a shit. They wouldn\'t.')
    c('The few people that would feel obligated to go to your funeral would')
    c('probably be annoyed and leave as early as possible.')
    c('That\'s who you are.')
    c('That\'s what you are')
    c('You\'re nothing to anyone. To everyone.')

def shortCheat():
    c('void Trigger()')
    c('{')
    c('DWORD EnemyInCH = Mem.Read<DWORD>(ClientDLL + EntityBase + ((CrossHairID - 1) * EntLoopDist));')
    c('int EnemyHealth = Mem.Read<int>(EnemyInCH + healthOffset);')
    c('int EnemyTeam = Mem.Read<int>(EnemyInCH + teamOffset);')
    c('if (LocalTeam != EnemyTeam && EnemyHealth > 0)')
    c('{')
    c('mouse_event(MOUSEEVENTF_LEFTDOWN, NULL, NULL, NULL, NULL);')
    c('mouse_event(MOUSEEVENTF_LEFTUP, NULL, NULL, NULL, NULL);')
    c('}')

def longCheat():
    c('#include "ProcMem.h"')
    c('ProcMem Mem;')
    c('Mem.Process("csgo.exe");')
    c('DWORD ClientDLL = Mem.Module("client.dll");')
    c('const DWORD playerBase = 0xA68A14;')
    c('const DWORD entityBase = 0x4A0B0C4;')
    c('const DWORD crosshairOffset = 0x23F8;')
    c('const DWORD teamOffset = 0xF0;')
    c('const DWORD healthOffset = 0xFC;')
    c('const DWORD EntLoopDist = 0x10;')
    c('DWORD LocalPlayer = Mem.Read<DWORD>(ClientDLL + PlayerBase);')
    c('int LocalTeam = Mem.Read<int>(LocalPlayer + teamOffset);')
    c('int CrossHairID = Mem.Read<int>(LocalPlayer + CrosshairOffset);')
    c('void Trigger()')
    c('{')
    c('DWORD EnemyInCH = Mem.Read<DWORD>(ClientDLL + EntityBase + ((CrossHairID - 1) * EntLoopDist));')
    c('int EnemyHealth = Mem.Read<int>(EnemyInCH + healthOffset); // Enemy in crosshair\'s')
    c('int EnemyTeam = Mem.Read<int>(EnemyInCH + teamOffset);')
    c('if (LocalTeam != EnemyTeam && EnemyHealth > 0)')
    c('mouse_event(MOUSEEVENTF_LEFTDOWN, NULL, NULL, NULL, NULL);')
    c('mouse_event(MOUSEEVENTF_LEFTUP, NULL, NULL, NULL, NULL);')
    c('}')
    c('int main()')
    c('{')
    c('    while(true)')
    c('    {')
    c('        Trigger();')
    c('        Sleep(0.1)')
    c('    }')
    c('}')

def wiki():
    i = 0
    text = ''

    url = ('https://en.wikipedia.org/wiki/' + pyautogui.prompt('enter keyword'))
    res = requests.get(url)
    res.raise_for_status()
    wikiPage = bs4.BeautifulSoup(res.text, "html.parser")
    wiki = wikiPage.select('p')
    para = wiki[0].getText()
    charArray = list(para)
    print (para)

    for d in charArray:
        text += d
        if d == ' ':
            i += 1

            if (i == 7):
                print(text)
                c(text)
                i = 0
                text = ''

    c(text)


option = pyautogui.prompt('1: profileSkim, 2: lobbyInfo, 3: fakeInfo, 4: explain webscraper, 5: fakeHacks, 6: fake ipAddr, 7: metasploit, 8: github link, 9: tcp, 10: mrRobot, 11: shortCheat, 12: longCheat, 13: wiki search')

if(option == '1'):
    profileSkim()
elif (option == '2'):
    lobbied()
elif (option == '3'):
    fakeInfo()
elif (option == '4'):
    explain()
elif (option == '5'):
    fakeHacks()
elif (option == '6'):
    fakeIPs()
elif (option == '7'):
    metasploit()
elif (option == '8'):
    github()
elif (option == '9'):
    tcp()
elif (option == '10'):
    mrRobot()
elif (option == '11'):
    shortCheat()
elif (option == '12'):
    longCheat()
elif (option == '13'):
    wiki()
else:
    print('nothing chosen')

import pyautogui, time, pyperclip
from random import shuffle
import webbrowser, sys, pyperclip, requests, bs4, re, time, getopt
name = 'User'
urlArray = []

def copy(two):
    pyautogui.click(629, two)
    pyautogui.click(710, two + 38)  # click steam profile
    time.sleep(2.5)
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

top()
#bottom()




try:

    default = 0.1
    #name = pyperclip.paste()
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


        resFriends = requests.get(urlArray[z] + '/friends')
        userFriends = bs4.BeautifulSoup(resFriends.text, "html.parser")
        usersName = userFriends.select('.whiteLink')
        elemsFriends = userFriends.select('.friendBlockContent')

        user = userProfile.select('.actual_persona_name')
        name = user[0].getText().strip()

        hours = userProfile.select('.game_info_details')




        print ('steam user: ' + name + '\t', end='')

        try:
            print(re.sub("Currently In-Game.*", "", hours[0].getText()).strip())
        except:
            print('private profile')
        print()

        for j in range(len(elemsFriends)):
            for k in range(len(nameArray)):
                if ((re.sub("\n.*", "", elemsFriends[j].getText().strip())) == nameArray[k]):
                    print ('\t' + re.sub("\n.*", "", elemsFriends[j].getText().strip()))


        print()
        print()

except:
    print ('error')

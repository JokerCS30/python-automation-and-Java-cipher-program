import pyautogui, time, pyperclip
from random import shuffle
import webbrowser, sys, pyperclip, requests, bs4, re, time, getopt
name = 'User'

def p(one, two):
    pyautogui.click(one, two)
    time.sleep(0.2)

def c(writing):
    pyautogui.click(255, 74)
    pyautogui.typewrite(writing)
    pyautogui.click(922, 595)

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

        p(238, 197)
        p(255, 74)      # text button
        pyautogui.typewrite('Steam URL: ' + steamURL)
        p(922, 595)     # ok button
        p(247, 283)
        c('Steam Name: ' + name)
        p(247, 377)
        c('10 steam friends off list: ')
        p(247, 465)
        c(re.sub("\n.*", "", elemsFriends[0].getText().strip()))
        p(247, 550)
        c(re.sub("\n.*", "", elemsFriends[1].getText().strip()))
        p(247, 646)
        c(re.sub("\n.*", "", elemsFriends[2].getText().strip()))
        p(247, 650)
        c(re.sub("\n.*", "", elemsFriends[3].getText().strip()))
        p(247, 652)
        c(re.sub("\n.*", "", elemsFriends[4].getText().strip()))
        p(247, 650)
        c(re.sub("\n.*", "", elemsFriends[5].getText().strip()))
        p(247, 650)
        c(re.sub("\n.*", "", elemsFriends[6].getText().strip()))
        p(247, 650)
        c(re.sub("\n.*", "", elemsFriends[7].getText().strip()))
        p(247, 650)
        c(re.sub("\n.*", "", elemsFriends[8].getText().strip()))
        p(247, 650)
        c(re.sub("\n.*", "", elemsFriends[9].getText().strip()))
        p(247, 693)
        c('TOR torch search engine results for steam user: ' + name)
        p(247, 766)
        c('December 2016 steam database leak. Search results for username: ' + name)
        p(247, 836)
        c('Results = one. please subscribe to our services for the raw data.')
        p(247, 910)
        c('href=\'trz899adafzf900af0.onion\'')















        break



        #for j in range(10):
            #loopText(re.sub("\n.*", "", elemsFriends[j].getText().strip()), 0)


except KeyboardInterrupt:
    print('done')

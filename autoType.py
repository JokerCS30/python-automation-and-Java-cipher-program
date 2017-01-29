import pyautogui, time, pyperclip
from random import shuffle
import webbrowser, sys, pyperclip, requests, bs4, re, time, getopt
name = 'User'

try:
    while True:
        default = 0.1
        #name = pyperclip.paste()
        steamURL = pyperclip.paste()
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



        def loopText(writing, interval):
            pyautogui.click(1035, 780)
            pyautogui.typewrite(writing)
            pyautogui.press('enter')
            time.sleep(interval)

        loopText('Skimming SteamUsers profile', default)
        loopText('Steam user url: ' + steamURL, default)
        loopText('Steam profile name: ' + name, default)

        try:
            resGroups = requests.get(steamURL + '/groups/')
            print('getting group url worked')
            userGroups = bs4.BeautifulSoup(resGroups.text, "html.parser")
            print('parsing group url worked')
            elemGroups = userGroups.select('.linkStandard')
            print('selection .linkstandard worked')

            firstGroup = elemGroups[0].getText().strip()
            print('grabbing firstgroup worked')
            loopText('first group: ' + firstGroup, default)

        except:
            loopText('User has no steam groups', 0)






        loopText('Users Friends: ', default)
        for j in range(len(elemsFriends)):
            loopText(re.sub("\n.*", "", elemsFriends[j].getText().strip()), 0)

        loopText('Most played game website: ', 0)
        webbrowser.open(steamURL + '/games/?tab=all')
        time.sleep(4)
        pyautogui.click(724, 464)
        time.sleep(0.2)
        pyautogui.click(750, 564)
        time.sleep(3)
        pyautogui.moveTo(573, 45)
        pyautogui.dragTo(121, 45)
        pyautogui.click(173, 44, button='right')
        pyautogui.click(320, 127)
        pyautogui.click(1894, 7)
        pyautogui.click(1012, 768)


        loopText(pyperclip.paste(), default)




        loopText('establishing connection', 5)
        loopText('Successful connection established with SteamUser: ' + name, default)
        loopText('Harvesting credentials using netcat & setToolKit...', 1)

        for x in range(10):
            loopText('...', 1)

        loopText('setting RPORT = 5543', default)
        loopText('sys.popen(\'service postgresql start\')', default)
        loopText('msfconsole', default)
        loopText('use exploit/windows/http/solarwinds_fsm_userlogin', default)
        loopText('set VHOST ' + name + '.getIP()', default)
        loopText('run', default)
        loopText('Exploit completed session created db_session/' + name + '_INFO', default)
        loopText('exit msfconsole', default)
        loopText('steamCredentialHarvester sch = new steamCredentialHarvester(' + name + '_INFO); ', default)
        loopText('sch.getAuthentication() >&1 /profiles/' + name, default)

        loopText('cracking m25 HashSums:', default)

        for z in range(30):
            shuffle(hexArray)
            hash = ''
            for word in hexArray:
                hash += word + ' '

            loopText(hash, 0)



        loopText('sch.send2FA(0220145297)',default)
        loopText('sch.reassignEmail()', default)
        loopText('sch.close()', default)
        loopText('run autoCloseLog', 1)
        loopText('erasing steam and user logs...', 1)

        for x in range(10):
            loopText('...', 1)

        loopText('all logs successfully erased, safe to close connection', default)
        loopText('close.connection()', default)
        loopText('closing connection with SteamUser: ' + name, 3)
        loopText('All information and credentials gathered can be found in root/aptLogs', default)
        break

except KeyboardInterrupt:
    print('\ndone.')
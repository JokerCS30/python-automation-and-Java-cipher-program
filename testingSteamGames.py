import pyautogui, time, pyperclip
from random import shuffle
import webbrowser, sys, pyperclip, requests, bs4, re, time, getopt

steamURL = 'http://steamcommunity.com/id/compowchicken'

res = requests.get(steamURL)
res.raise_for_status()
userProfile = bs4.BeautifulSoup(res.text, "html.parser")


resFriends = requests.get(steamURL + '/friends')
userFriends = bs4.BeautifulSoup(resFriends.text, "html.parser")
usersName = userFriends.select('.whiteLink')
elemsFriends = userFriends.select('.friendBlockContent')

print ('first friend: ' + elemsFriends[0].getText().strip())

print ('name: ' + usersName[0].getText().strip())

resGames = requests.get(steamURL + '/games/?tab=all')
userGames = bs4.BeautifulSoup(resGames.text, "html.parser")


elemGames = userGames.select('.gameListRow')
#mostPlayed = elemGames[0].getText().strip()

name = usersName[0].getText().strip()


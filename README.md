# CSGO-chat-automation-scripts
python scripts to automate things in csgo, mainly creating macros

Mainly using Beautiful Soup and pyautogui these scripts will create macros, webscrape info, auto steam message, auto shoot, spin etc

Scripts and their functions:

autoType.py:

this script is meant for steam message where you must copy the steam page url and then using pyperclip.paste() it will automatically assign the steam url from the clipboard. Using Beautiful Soup it parses the html data and then grabs what info I choose by selecting an element eg: for users name userFriends.select('.whiteLink'), .whiteLink is the name of the class which contains the users profile name. 
Does the same thing with the users friends but using the url + /friend. Had trouble selecting the element for most played game for some reason. Class name didn't seem to work and I opted instead for opening the page itself and using pyautogui to go to the games website and copy paste it. loopText method is used to automate clicking into the steam message box and writing what message is passed as a parameter, presses enter then sleep which I set the default value to 0.1. Had to place the steam friends and game info inside try block incase the profile is private so it doesn't auto crash the script. After the steam profile info it just writes text I've manually written into the script, the fake msfconsole type commands etc. Hashsum crack is very incorrect but I purely did it to fit within message box neatly. For some reason 

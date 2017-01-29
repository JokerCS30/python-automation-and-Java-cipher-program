import sys
import re
from string import ascii_lowercase
import operator

message = "the periodic table is a tabular arrangement of the chemical elements organised on the basis of their atomic numbers electron configurations and recurring chemical properties we’ve used it to create a cipher by using the initial letters of the elements but two letters cant be used what are they"
multiArray = [['']*3 for i in range(26)]

for i in range(len(multiArray)):
    multiArray[i][0] = i + 1

for i, c in enumerate(ascii_lowercase):             # assigning each letter of the alphabet to first index of multiArray
    multiArray[i][1] = c

for i, c in enumerate(message):
    for z in range(len(multiArray)):
        if c == multiArray[z][1]:
            if multiArray[z][2] == '':
                multiArray[z][2] = 1

            else:
                count = int(multiArray[z][2]) + 1
                multiArray[z][2] = count

print(multiArray)






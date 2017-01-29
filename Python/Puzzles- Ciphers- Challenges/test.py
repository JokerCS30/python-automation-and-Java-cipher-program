import sys
from string import ascii_lowercase
import operator

message = 'this message will be encrypted with a special cipher which I wanted to use to test my decipher code on. If theres lots of letters it should work alot more accurately. The message will be the answer'

letter_dict = [['a']*4 for i in range(26)]

message = message.lower()

for i, c in enumerate(ascii_lowercase):
    letter_dict[i][0] = c
    letter_dict[i][1] = (i + 1)
    letter_dict[i][3] = (i + 8)
    if letter_dict[i][3] > 26:
        letter_dict[i][3] = letter_dict[i][3] - 26

print (letter_dict)

letter_dict = (sorted(letter_dict, key=operator.itemgetter(3), reverse=False))
for i, c in enumerate(ascii_lowercase):
    letter_dict[i][2] = c

for i, c in enumerate(message):
   if c == ' ':
       sys.stdout.write(' ')

   else:
       for i in range(len(letter_dict)):
           if c == letter_dict[i][0]:
               sys.stdout.write(letter_dict[i][2])
















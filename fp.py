# Task
'''
1. read the arp table
2. look for one mac address associated with multiple IPs
3. ignore headers and broadcast address
# simulate attack using static route
arp -s 157.55.85.211   00-aa-00-62-c6-09
arp -s 157.55.85.212   00-aa-00-62-c6-09
'''
# arp table poison
# look for different ip, but same mac-address
import os
import collections
import myfunction
detective_dictionary = collections.defaultdict(list)


def extract_arp_table():
    global each_line
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    each_line = []
    for line in arp_table_lines:
        each_line.append(line.split())
    return each_line

# get the arp table from a windows machine
# note, for a linux, data formatting could be little different
get_arp_table_list = extract_arp_table()

# for l in each_line:
#     print(l)

# def arp_spoof_dictionary():
#     for item in get_arp_table_list:
#         # print(item)
#         if len(item) == 3 and item[1] != "ff-ff-ff-ff-ff-ff":
#             # check for duplicate in list
#             # print(item[0], item[1])
#             # if IP address not in the list, add to the list
#             if item[0] not in detective_dictionary[item[1]]:
#                 detective_dictionary[item[1]].append(item[0])


dict = myfunction.arp_spoof_dictionary(get_arp_table_list)
print(type(dict))
print(dict)

#
#
# print(detective_dictionary)

for key,value in dict.items():
    if (len(value) > 1):
        print(f'Yes, spoofing detected, mac-adress spoofed is {key} and problem ips are {value}')


#
# do we have any duplicate?
# Flag again
spoofing = False

for key, value in detective_dictionary.items():
    # print(len(value))
    if len(value) > 1:
        spoofing = True
        print(" Arp Spoofing Detected!!")

# print(spoofing)
# print(detective_dictionary)

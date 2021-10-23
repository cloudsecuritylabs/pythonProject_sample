import os
import collections
import myfunction

# step 2
arp_table = os.popen("arp -a").read()
arp_table_lines = arp_table.splitlines()

# print(type(arp_table_lines))
# print(arp_table_lines[5].split())

# for line in arp_table_lines:
#     print(line)

# alternate way to save the file in a txt file
os.system('arp -a > "arptable.txt"')
arptable_file = open("arptable.txt", "r")

detective_dictionary = collections.defaultdict(list)


for line in arptable_file:
    split = line.split()
    # print(split)
    # print(len(split))
    if len(split) == 3:
        print(split[0])
        print(split[1])
        if split[0] not in detective_dictionary[split[1]]:
            detective_dictionary[split[1]].append(split[0])
        # detective_dictionary[split[1]] = detective_dictionary[split[1]].append(split[0])

    # splitted = line.split(",")
    # if(len(splitted) == 3):
    #
    #     print(splitted)
    #     print(splitted[1])
    #     print(splitted[0])
    #     # print(line.split())
    #     detective_dictionaty[splitted[1]] = ip_list.append(splitted[0])

print(detective_dictionary)



#


import collections
detective_dictionary = collections.defaultdict(list)
# get_arp_table_list =[]
def arp_spoof_dictionary(get_arp_table_list):
    for item in get_arp_table_list:
        # print(item)
        if len(item) == 3 and item[1] != "ff-ff-ff-ff-ff-ff":
            # check for duplicate in list
            # print(item[0], item[1])
            # if IP address not in the list, add to the list
            if item[0] not in detective_dictionary[item[1]]:
                detective_dictionary[item[1]].append(item[0])
    return detective_dictionary
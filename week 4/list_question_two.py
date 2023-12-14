# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
#
# list3 = [list1[0]+list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]]

def concat_two_list():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    list_result = []

    for i in range (0,len(list1),1):
        list_result.append(list1[i] + list2[i])

    return list_result

list1 = concat_two_list()
print(list1)
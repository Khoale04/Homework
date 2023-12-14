
def concat_two_list():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    list_result = []

    for i in range (0,len(list1),1):
        list_result.append(list1[i] + list2[i])
    return list_result

list1 = concat_two_list()

print(list1)


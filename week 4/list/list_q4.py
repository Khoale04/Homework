# Concatenate two lists in the following order
# Given:
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate_list(list1, list2):
    result_list = []
    for i in list1:
        for j in list2:
            result = i + " " + j
            result_list.append(result)
    return result_list

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
final_list = concatenate_list(list1,list2)
print(final_list)
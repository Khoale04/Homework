# Iterate both lists simultaneously. Given a two Python list.
# Write a program to iterate both lists simultaneously and
# display items from list1 in original order and items from list2 in reverse order.
# Given:
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Output:
# 10 400
# 20 300
# 30 200
# 40 100

def iterate_list(list1,list2):
    for i in range(0,len(list1),1):
        print(list1[i], end = " ")
        print(list2[-1-i])

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_list(list1,list2)
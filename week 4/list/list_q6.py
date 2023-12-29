# Add new item to list after a specified item.
# Write a program to add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# def add_new_item():
def add_new_item(list1):
    for i in list1:
        if type(i) == list:
            for j in i:
                if type(j) == list:
                    for k in j:
                        if type(k) == list:
                            print(k)
                        else:
                            if k == 6000:
                                j.append(7000)
                else:
                    if j == 6000:
                        i.append(7000)
        else:
            if i == 6000:
                list1.append(7000)
    return list1



list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
result_list = add_new_item(list1)
print(result_list)
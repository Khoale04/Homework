def concat_two_list():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    list3 = list2[::-1]
    list_result = []

    for i in range(0,len(list1),1):
        list_result.append(list1[i])
        list_result.append(list3[i])


    return list_result

list = concat_two_list()
print(list)
#không biết xuống dòng giống output của đề



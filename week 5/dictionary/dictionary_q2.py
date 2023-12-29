dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def merge_dictionary(dict1, dict2):
    dict3 = {}
    for i in dict1.keys():
        dict3[i] = dict1[i]

    for j in dict2.keys():
        dict3[j] = dict2[j]
# dict1['key'] = value

    return dict3

result = merge_dictionary(dict1,dict2)
print(result)
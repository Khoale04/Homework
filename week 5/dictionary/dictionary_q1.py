# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
#
# dictionary = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# print(dictionary.keys())
#
# dictionary = {}
# for i in keys:
#     dictionary.keys() = i
# dictionary["Ten"] = 10
# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())



# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dictionary = {}
# for i in range(0,len(keys),1):
#     dictionary[keys[i]] = values[i]
#     print(dictionary)
    # print(i)
    # print(keys[i])

def create_dictionary(keys,values):
    dictionary = {}
    for i in range(0, len(keys), 1):
        dictionary[keys[i]] = values[i]
    return dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

a = create_dictionary(keys,values)
print(a)
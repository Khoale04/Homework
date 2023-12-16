
def arrange_list(input):
    lower = ""
    upper = ""
    for i in input:
        if i.islower():
            lower += i
        else:
            upper += i
    result_str = lower + upper
    return result_str

str1 = "PyThoN"
print(arrange_list(str1))



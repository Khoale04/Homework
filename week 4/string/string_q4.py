def number_of_item(str1):
    char = 0
    digit = 0
    symbol = 0

    for i in str1:
        if i.isdigit():
            digit += 1
        else:
            if i.isalpha():
                char += 1
            else:
                symbol += 1
    return char, digit, symbol


str1 = "P@#yn26at^&i5ve"
result = number_of_item(str1)
print("character = ", result[0], "digit = ", result[1], "symbol = ", result[2], end="\n")


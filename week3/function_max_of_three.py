def max_of_three(num_1, num_2, num_3):
    maximum = 0
    if num_1 > num_2 and num_1 > num_2:
        print(num_1, "is max")
        max_number = num_1
    else:
        if num_2 > num_1 and num_2 > num_3:
            print(num_2, "is max")
            max_number = num_2
        else:
            print(num_3, "is max")
            max_number = num_3
    return max_number


#input number
number_1 = input("please insert number 1: ")
number_2 = input("please insert number 2: ")
number_3 = input("please insert number 3: ")

#validate input
if number_1.isdigit() and number_2.isdigit() and number_3.isdigit():
    number_1 = int(number_1)
    number_2 = int(number_2)
    number_3 = int(number_3)
    maximum = max_of_three(number_1, number_2, number_3)
    print("the maximum is ", maximum)
else:
    print("this is not valid")




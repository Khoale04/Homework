def even_or_odd(number):
    if number%2==0 and number>0:
        print("it is an even number")
    else:
        print("it is an odd")

user_number = int(input("please input a number"))
even_or_odd(user_number)


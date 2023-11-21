import random

rand_num = random.randint(1, 10)
print("random number " + str(rand_num))
str_number = input("What's your number ")
number = int(str_number)
print(number)
result = rand_num == number
print(result)

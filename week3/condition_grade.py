def grade(number):
    if 79 < int(number) <= 100:
        print("Your result is HD")
    else:
        if 70 <= int(number) <= 79:
            print("Your result is DI")
        else:
            if 60 <= int(number) <= 69:
                print("Your result is CR")
            else:
                if 50 <= int(number) <= 59:
                    print("Your result is PA")
                else:
                    if 0 <= int(number) <= 49:
                        print("Your result is NN")
                    else:
                        print("in valid")
    return grade
#user input
user_input = input("Please input your grade: ")

#vadilate input
if user_input.isdigit():
    user_grade = grade(user_input)
else:
    print("please enter a accurate number")


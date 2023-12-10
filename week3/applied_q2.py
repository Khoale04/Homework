def number(n):
    previous_number = 1
    for number in range(1,n):
        # dòng đầu là ngoại le cho number va previous number
        if number == 1:
            print(number, previous_number)
        else:
            print(number, previous_number + number,end=" ")
            print()
            previous_number = number + previous_number



number(6)

# def number_pattern(n):
#     for number in range(n+1):
#         print(number, end=' ')
#
#     print('')
#
#     for number in range(n):
#         print(number, end=' ')
#
#     print()
#     for number in range(n-1):
#         print(number, end=' ')
#
#     print()
#     for number in range(n-2):
#         print(number, end=' ')
#
#     print()
#     for number in range(n-3):
#         print(number, end=' ')
#
#     print()
#     for number in range(n-4):
#         print(number, end=' ')

def new_number(n):
    for new_number in range(n+1):
        for number in range(n + 1 - new_number):
            print(number, end=' ')
        print()

# number_pattern(5)
new_number(5)

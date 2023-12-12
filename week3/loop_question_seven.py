# def calculate_number(n):
#     previous_total = 0
#     total = 0
#     for current_number in range(1, n+1, 1):
#             total = previous_total + current_number
#             previous_total = total
#             print(total)
#     return total

def calculate_sum(n):
    previous = ""
    after = ""
    total = 0
    previous_total = 0


    for two in range(0,n):
            after = previous + "2"
            previous = after
            # print(previous)

            total = int(previous) + previous_total
            previous_total = total
            # print(total)
    return total

test = calculate_sum(5)
testt = test +2
print(calculate_sum(5))
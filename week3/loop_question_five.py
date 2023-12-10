def calculate_number(n):
    previous_total = 1
    total = 1
    for current_number in range(1, n+1, 1):
            total = previous_total * current_number
            previous_total = total
            print(total)
    return total
calculate_number(3)
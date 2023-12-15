
def square_number():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    result = []
    for i in range(0,len(numbers),1):
        result.append(numbers[i]**2)
    return result


result = square_number()
print(result)



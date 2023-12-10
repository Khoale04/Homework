def display_day_name(day_number):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if 1 <= day_number <= 7:
        day_name = days_of_week[day_number - 1]
        print(f"The day corresponding to {day_number} is {day_name}.")
    else:
        print("Invalid input. Please enter a number between 1 and 7.")

# Example usage:
user_input = int(input("Enter a number from 1 to 7: "))
display_day_name(user_input)

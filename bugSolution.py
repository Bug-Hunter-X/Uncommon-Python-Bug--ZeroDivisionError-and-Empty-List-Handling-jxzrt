def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if all(x == 0 for x in numbers):
        return 0  # Handle all zeros case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_numbers_with_zero = [10, 0, 20, 30, 40, 50]
average_zero = calculate_average(my_numbers_with_zero)
print(f"The average of a list with 0 is: {average_zero}")

my_all_zeros = [0, 0, 0]
average_all_zeros = calculate_average(my_all_zeros)
print(f"The average of all zeros is: {average_all_zeros}")

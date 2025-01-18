def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}")

# Example with a list of numbers
number_list = [10, 20, 30, 40, 50]
average = calculate_average(number_list)
print(f"Average: {average}")

#Example with a list containing non-numbers
number_list = [10, 20, 'a', 40, 50]
average = calculate_average(number_list)
print(f"Average: {average}")

# Example with a list containing only non-numbers
number_list = ['a', 'b', 'c']
average = calculate_average(number_list)
print(f"Average: {average}")

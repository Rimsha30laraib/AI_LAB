# Task 1: Introduction
print("Welcome to the Python Program which calculates the average of the numbers")

# Task 2: Terminal
print(" This Program is going to run in terminal.")

# Task 3: Python Interpreter
print("You can run this program using the Python interpreter.")

# Task 4: Variables
numbers = [1, 2, 3, 4, 5]

# Task 5: Text Editor
print("Using VS Code as a text editor.")

# Task 6: Functions
def calculate_average(nums):
    total = sum(nums)
    average = total / len(nums)
    return average

# Task 7: Lists and Tuples
print("List of numbers:", numbers)

# Task 8: Conditional Statements
if len(numbers) > 0:
    # Task 9: The For Loop
    for num in numbers:
        print("Number:", num)
else:
    print("The list is empty.")

# Task 10: User Input and the While Loop
user_input = input("Do you want to add more numbers? (yes/no): ")

while user_input.lower() == 'yes':
    new_number = int(input("Enter a number: "))
    numbers.append(new_number)
    print(numbers)
    user_input = input("Do you want to add more numbers? (yes/no): ")

average_result = calculate_average(numbers)
print("Average of the numbers:", average_result)

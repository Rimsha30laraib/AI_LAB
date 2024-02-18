#a Python program to find if a given string starts with a given character using Lambda. 

check_startswith = lambda string, char: string.startswith(char)

# Example usage
input_string = input("Enter a string: ")
start_char = input("Enter the character to check for: ")

result = check_startswith(input_string, start_char)

print(f"Does the string start with the character? {result}")

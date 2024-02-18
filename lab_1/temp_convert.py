# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
celsius_temp = float(input("Enter temp in Celsius: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

print("Temperature in Fahrenheit is:", fahrenheit_temp, "°F")

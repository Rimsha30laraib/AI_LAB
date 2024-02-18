#You have collected information about cities in your province. You decide to store each city’s name, population, and mayor in a file. Write a python program to accept the data for a number of cities from the keyboard and store the data in a file in the order in which they’re entered.

num_cities = int(input("Enter the number of cities: "))

file= open("city_data.txt","a") 
for i in range(num_cities):
    city_name = input("Enter city name: ")
    city_population = int(input("Enter city population: "))
    city_mayor = input("Enter city mayor name: ")
    file.write(f"City Name: {city_name}, Population: {city_population}, Mayor: {city_mayor}\n")
print("City data has been successfully written to city_data.txt.")

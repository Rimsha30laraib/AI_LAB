time_taken = int(input("Enter the time taken by the worker to complete the job (in hours): "))

if 2 <= time_taken <= 3:
    efficiency = "Highly Efficient"
elif 3 < time_taken <= 4:
    efficiency = "Improve Speed"
elif 4 < time_taken <= 5:
    efficiency = "Training Required"
elif time_taken > 5:
    efficiency = "Leave the Company"
else:
    efficiency = "Invalid input"

print("Efficiency of the worker:", efficiency)


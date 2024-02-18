# a Python program to square and cube every number in a given listist of integers using listambda.

list=[2,3,4,5]
squares=[]
cubes=[]
for i in range (len(list)):
    y=lambda x:x**2
    squares.append(y(list[i]))
    b=lambda z:z**3
    cubes.append(b(list[i]))

print("list of a number are: ",list)
print("Square of a list are: ", squares)
print("Cube of a list are: ", cubes)

#CHECK THE PASSWORD IS RIGHT OR NOT
password = input("What is the password? ")

if password == "abc$123" or password == "ABC$123":
    print("Welcome!")
else:
    print("I don't know you")

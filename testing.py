name = input("Enter your name: ")
age = int(input("What is the year that you was born: "))
if name:
    print(f"Hi {name} how are you!")
    if age:
        print(f"You have {- age + 2026} years old")
else:
    print("Please enter your name")
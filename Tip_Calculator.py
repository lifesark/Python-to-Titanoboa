print("Welcome to the tip calculator!")
a = float(input("What was the total amount? \n$"))
b = float(input("How much percentage of tip would you like to give? \n"))
c = float(input("How many people to split the bill?\n"))
d = (a/c)*(1.00+(b/100))
print(f"Each person should pay: ${round(d,2)}\n")
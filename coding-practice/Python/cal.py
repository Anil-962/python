a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    print(f"Addition of 2 numbers is {a+b}")
elif operator == '-':
    print(f"Subtraction of 2 numbers is {a-b}")  
elif operator == '*':
    print(f"Multiplication of 2 numbers is {a*b}")
elif operator == '/':
    print(f"Division of 2 numbers is {a/b}")
else:
    print("Invalid operator")
a = input("Enter a any number between 1 and 10: ")
if a < 1 or a > 10:
    raise ValueError("The number is out of range. Please enter a number between 1 and 10.")
else:
    print("Thank you! You entered:", a)
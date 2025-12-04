a=input("Enter the a number: ")
print(f"The Multiplication of {a}is:")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except Exception as e:
    print("Please enter a valid number")
finally:
    print("Thank you for using the multiplication table generator.")
    
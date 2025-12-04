a = int(input("Enter a:"))
b = int(input("Enter b:"))
"""print("Before swapping a:",a)
print("Before swapping b:",b)
temp = a
a=b
b=temp
print("After swapping a:",a)
print("After swapping b:",b)"""
a = a+b
b = a-b
a = a-b
print(f"After swapping a: {a}")
print(f"After swapping b: {b}")
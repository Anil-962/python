#a,b,c
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
root1 = 0
root2 = 0
d = (b**2) - (4*a*c)
root1 =(-b + (d**(0.5)))/(2*a)
root2 =(-b - (d**(0.5)))/(2*a)
##print("Root1:",root1)
#print("Root2:",root2)
#d = (b**2) - (4*a*c)
print(f"Roots:({root1},{root2})")


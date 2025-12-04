# def calculate(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# a = 4
# b = 5
# calculate(a,b)
# c = 7
# d = 6

# calculate(c,d) 


# Using Function finding Greatest Number
# def isGreatest(a,b):
#     if a>b:
#         print(f'{a} is greatest')
#     else:
#         print(f'{b} is greatest')
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# isGreatest(a,b)
# c= int(input('Enter first number: '))
# d= int(input('Enter second number: '))
# isGreatest(c,d)


def name(**name):
    print("Hello",name['fname'],name['lname'])
# name(fname="John",lname="Doe")
fname = input('Enter first name: ')
lname = input('Enter last name: ')
name(fname=fname,lname=lname)
m = int(input("Enter the maths marks: "))
s = int(input("Enter the Science marks: "))
e = int(input("Enter the English marks: "))

Total = m+s+e
avg = Total/3
per = (Total/300)*100
print(Total)
print(per)
print(avg)
if avg>=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")        
elif avg>=60:
    print("Grade D")
    
elif avg>=40:
    print("Grade E")
else:
    print("Grade F")


    
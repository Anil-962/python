import time
t = time.strftime('%H:%M:%S')
print(t)
H = int(time.strftime('%H'))
H = int(input(time.strftime('%H\n')))
print(H)

if (H>=0 and H<12):
    print("Good Morning")
elif(H>=12 and H<16):
    print("Good Afternoon")
elif(H>=16 and H<20):   
    print("Good Evening")
elif(H>=20 and H<=23):
    print("Good Night")
 
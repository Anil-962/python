w = input("Enter the weather: ")
day = input()
if w == "Sunny":
    if day == "day":
      print("It's a sunny day")
    else:
        print("It's a sunny night")
elif w == "Rainy":
    print("It's a rainy day")
elif w == "Cloudy" and day =="night":
    if day == "night":
        print("It's a cloudy day")
    else:
      print("It's a cloudy night")
else:
    print("It's not a sunny day")
print("Have a nice day")
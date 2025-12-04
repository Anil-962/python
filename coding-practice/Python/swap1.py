from string import ascii_lowercase, ascii_uppercase


a = str(input())
temp = ascii_uppercase()
ascii_uppercase = ascii_lowercase()
ascii_lowercase = temp
print(ascii_uppercase)

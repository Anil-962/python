# f =open("Hello.py","r")
# print(f)
# print("File Name:",f.name)
# print("File Mode:",f.mode)
# content = f.read()
# print(content)
# f.close()


# writeing File
with open("Hello.txt","w") as file:
    file.write("Hello World\n")
    file.write("Welcome to Python Programming")
print("File written successfully")
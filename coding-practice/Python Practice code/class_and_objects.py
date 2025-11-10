

# 1.Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created
# emp = Employee(1, "coder")
# 2.Use del property to first delete id attribute and then the entire object

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(self.id, self.name)

emp = Employee(1, "coder")
emp.display()

del emp.id
try:
    print(emp.id)
except NameError:
  print("NameError: name 'id' is not defined")
del emp
try:
  emp.display()
except NameError:
  print("NameError: name 'emp' is not defined")

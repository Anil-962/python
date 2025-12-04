# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# Dog1 = Dog("Chandhu",5)
# print(f'Doog name is:{Dog1.name}and age={Dog1.age}')


# Employee details
class Employee:
    def __init__(self,name,salary):
        self.name = name
        #self._salary = salary
        self.__salary = salary
    def salary_info(self):
        return self.__salary
emp = Employee("Anil",50000)
print(f'Employee Name: {emp.name}')
print(f'Employee Salary: {emp.salary_info()}')
# print(f'Employee Salary: {emp.__salary}') # This will raise an AttributeError 
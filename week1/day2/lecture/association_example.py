class Department():
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []
        #^^ this will be an empty list (array) FOR NOW

    def add_employee (self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
#this function prevents from the same employee being added to 
#to upper function so it doesn't add it to the list self.employees = []


class Employee():
    def __init__(self, first_name, last_name, salary, department, middle_name=None):
    #this is for creating an employee list
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
        self.department = department
        self.department.employees.append(self)

#We are now going to add a method called method
#purpose: return full name
    def full_name(self):
        if self.middle_name==None:  #None mustbe captial N, same as null
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

    def change_salary(self, percent_increase):

        if percent_increase > 10:
            return None

        new_salary = self.salary * (1 + (.1 * percent_increase))

        if not self.salary * (1 + percent_increase) < 40000:
            self.salary = new_salary

    def __repr__(self):
        return f"{self.first_name[0]}. {self.last_name}"
            

department_a = Department("Sales", "804A")
department_b = Department("Engineering", "201B")

employee_1 = Employee("Alex", "Smith", 82000, department_a)
employee_2 = Employee("Bradley", "Jones", 79000, department_a)
employee_3 = Employee("Charlie", "Adams", 65000, department_a)
employee_4 = Employee("Darla", "Smith", 85000, department_b, "Allison")
employee_4 = Employee("Erick", "Ortega", 97000, department_b, "Ricky")
# #this is creating the new employee

print(employee_1)
print(department_a.employees)
print(department_b.employees)



# employees = [employee_1, employee_2, employee_3, employee_4]

# # for employee in employees:
# #     if employee.middle_name == None:
# #         print(f"Full name: {employee.first_name} {employee.last_name} , salary: {employee.salary}")
# #     else:    
# #         print(f"Full name: {employee.first_name} {employee.middle_name} {employee.last_name} , salary: {employee.salary}")
# ##this here is just another way to check IF the person has a middlename

# for employee in employees:
#     print(f"Full name: {employee.full_name()}, salary: {employee.salary}")

# #Now to give the employees a 5% raise
# for employee in employees:
#     employee.change_salary(5)
#     # employee.salary = employee.salary * 1.05      DO NOT USE THIS METHOD

# print("\n\nAfter the percentage increase")
# for employee in employees:
#     print(f"Full name: {employee.full_name()}, salary: {employee.salary}")


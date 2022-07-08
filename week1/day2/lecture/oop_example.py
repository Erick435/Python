class Employee():
    def __init__(self, first_name, last_name, salary, middle_name=None):
    #this is for creating an employee list
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.middle_name = middle_name

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
            
employee_1 = Employee("Alex", "Smith", 82000)
employee_2 = Employee("Bradley", "Jones", 79000)
employee_3 = Employee("Charlie", "Adams", 65000)
employee_4 = Employee("Darla", "Smith", 85000, "Allison")
employee_4 = Employee("Erick", "Ortega", 97000, "Ricky")
#this is creating the new employee

employees = [employee_1, employee_2, employee_3, employee_4]

# for employee in employees:
#     if employee.middle_name == None:
#         print(f"Full name: {employee.first_name} {employee.last_name} , salary: {employee.salary}")
#     else:    
#         print(f"Full name: {employee.first_name} {employee.middle_name} {employee.last_name} , salary: {employee.salary}")
##this here is just another way to check IF the person has a middlename

for employee in employees:
    print(f"Full name: {employee.full_name()}, salary: {employee.salary}")

#Now to give the employees a 5% raise
for employee in employees:
    employee.change_salary(5)
    # employee.salary = employee.salary * 1.05      DO NOT USE THIS METHOD

print("\n\nAfter the percentage increase")
for employee in employees:
    print(f"Full name: {employee.full_name()}, salary: {employee.salary}")

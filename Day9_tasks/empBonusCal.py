'''
Employee Bonus Calculator (Decorators & OOP)
A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the salary by
adding a bonus before displaying it
'''
def add_bonus(func):
    def emp_salary(self):
        bonus = self.salary * 0.10   # 10% bonus
        self.salary += bonus
        func(self)
    return emp_salary

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display_salary(self):
        print(f"Employee: {self.name} \nSalary with Bonus: {self.salary}")

# Test
emp = Employee("Harsha", 50000)
emp.display_salary()
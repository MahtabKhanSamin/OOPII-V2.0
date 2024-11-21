class SalaryNotInRange(Exception):
    pass

class Employee:
    def __init__(self,a,b):
        self.name=a
        self.salary = b
    def display(self):
        if self.salary<10000 or self.salary>50000:
            raise SalaryNotInRange
        else:
            print("Current Salary: ",self.salary)
try:
    b=Employee("Mahtab", 40000)
    b.display()
    c=Employee("Sadman", 60000)
    c.display()
except SalaryNotInRange:
    print("Your Salary is not in Range")
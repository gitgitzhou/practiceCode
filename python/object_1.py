class Employee:
    # 'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount

emp3 = Employee("Johan", 6000)
emp3.displayCount()

emp3.age = 23
print "The age of Employee 3 is: %d" % emp3.age

print hasattr(emp3, 'age')

# print getattr(emp1, 'age')
print getattr(emp3, 'age')
print getattr(emp2, 'salary')


setattr(emp2, 'salary', 8000)
print getattr(emp2, 'salary')

delattr(emp2, 'salary')

print "\nEmployee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

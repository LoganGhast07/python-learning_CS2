#Problem 1: Employee Payroll System with Polymorphism
#Create an employee payroll system using abstract base classes and polymorphism. Different employee types calculate pay differently.
#Part A: Abstract Employee Class (15 points)
#Create an abstract Employee class with:
#1. Constructor that takes name and employee_id
#2. Abstract method calculate_pay() — each subclass computes pay differently
#3. Abstract method description() — returns a one-line summary of the employee
#4. Regular method pay_stub() that returns: "[name] (ID: [employee_id]): $[pay]" (calls
#   calculate_pay() internally — this is polymorphism!)
#5. Static method validate_positive(value, name) that:
#   Returns True if value > 0
#   Raises ValueError with message "[name] must be positive!" otherwise

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement calculate_pay()")

    def description(self):
        raise NotImplementedError("Subclasses must implement description()")

    def pay_stub(self):
        pay = self.calculate_pay()
        return f"{self.name} (ID: {self.employee_id}): ${pay:.2f}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        else:
            raise ValueError(f"{name} must be positive!")

#Part B: Concrete Employee Classes (25 points)
#Create three classes that inherit from Employee:
#SalariedEmployee:
##Constructor takes: name, employee_id, annual_salary
#Validate salary is positive using the static method
#calculate_pay() returns annual_salary / 24 (paid twice per month)
#description() returns "Salaried: [name]"
#HourlyEmployee:
##Constructor takes: name, employee_id, hourly_rate, hours_worked
#Validate rate and hours are positive
#calculate_pay() returns hourly_rate * hours_worked for the first 40 hours, plus hourly_rate *
#1.5 * overtime_hours for any hours beyond 40
#description() returns "Hourly: [name]"
#CommissionEmployee:
##Constructor takes: name, employee_id, base_salary, sales, commission_rate
#Validate all values are positive; commission_rate must also be ≤ 1.0
#calculate_pay() returns base_salary + (sales * commission_rate)
#description() returns "Commission: [name]"
class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        Employee.validate_positive(annual_salary, "Annual salary")
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 24

    def description(self):
        return f"Salaried: {self.name}"

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        Employee.validate_positive(hourly_rate, "Hourly rate")
        Employee.validate_positive(hours_worked, "Hours worked")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            overtime_hours = self.hours_worked - 40
            return (self.hourly_rate * 40) + (self.hourly_rate * 1.5 * overtime_hours)

    def description(self):
        return f"Hourly: {self.name}"

class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)
        Employee.validate_positive(base_salary, "Base salary")
        Employee.validate_positive(sales, "Sales")
        Employee.validate_positive(commission_rate, "Commission rate")
        if commission_rate > 1.0:
            raise ValueError("Commission rate must be positive!")
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_pay(self):
        return self.base_salary + (self.sales * self.commission_rate)

    def description(self):
        return f"Commission: {self.name}"

#Part C: Payroll Class (10 points)
#Create a Payroll class that:
#1. Stores a list of employees
#2. Method add_employee(employee) to add an employee
#3. Method total_payroll() that returns the sum of all employee pay
#4. Method print_all_stubs() that prints every employee's pay stub
#5. Uses polymorphism — doesn't care what type of employee!

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        return sum(employee.calculate_pay() for employee in self.employees)

    def print_all_stubs(self):
        for employee in self.employees:
            print(employee.pay_stub())


# Test your code
if __name__ == "__main__":
# Create employees
    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)
    # Test individual employees
    print("Employee Descriptions:")
    for emp in [alice, bob, carol]:
        print(f" {emp.description()}")
    print("\nPay Stubs:")
    for emp in [alice, bob, carol]:
        print(f" {emp.pay_stub()}")
# Test payroll (polymorphism!)
    payroll = Payroll()
    payroll.add_employee(alice)
    payroll.add_employee(bob)
    payroll.add_employee(carol)
    print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")
# Test validation
    print("\nTesting validation:")
    try:
        bad = SalariedEmployee("Bad", "E999", -50000)
    except ValueError as e:
        print(f" Caught: {e}")
    try:
        bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
    except ValueError as e:
        print(f" Caught: {e}")
'''Create a Python class called Employee to manage employee details and salary.

Your class should have the following requirements:
1. Create a class named Employee.
2. Initialize the following attributes using a constructor:
   - name
   - employee_id
   - salary
3. Create a method display_details() to display employee information.
4. Create a method increase_salary(amount) to increase the employee's salary.
5. Create a method get_salary() to return the current salary.
6. Make the salary variable private using double underscores (__salary).'''


class Employee:

    def __init__(self, name: str, employee_id: int, salary: int):
        # Attributes --> variables
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary

    def display_details(self):
        print("Employee name:", self.name)
        print("Employee ID", self.employee_id)
        print("Current Salary", self.__salary)

    def increase_salary(self, amount):
        self.__salary += amount
        print("Salary increased successfully!")

    def get_salary(self):
        return self.__salary


# creating object

e1 = Employee("Brajesh", 10, 65000)
e1.display_details()
e1.increase_salary(5000)
print("\nUpdated Salary is:",e1.get_salary())
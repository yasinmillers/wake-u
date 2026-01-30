class Employee:
    def calculate_salary(self):
        monthly_salary = 3000
        allowances = 500
        total = monthly_salary + allowances
        print(f"Total Salary: {total}")
class fulltimeEmployee(Employee):
    def calculate_salary(self):
        transport=1000
        allowance=500
        monthly_salary=4000
        food=800
        total = monthly_salary + transport + allowance + food
        print(f"Total Salary for Full-time Employee: {total}")
        
class ParttimeEmployee(Employee):
    def calculate_salary(self):
        hourly_rate = 20
        hours_worked = 80
        total = hourly_rate * hours_worked
        print(f"Total Salary for Part-time Employee: {total}")
        
        
s1=fulltimeEmployee()
s2=ParttimeEmployee()

s1.calculate_salary()
s2.calculate_salary()
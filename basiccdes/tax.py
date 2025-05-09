name = input("Enter employee name  : ")
emp_id = int(input("Enter employee id : "))
monthlySal = float(input("Enter your monhly salary : ")) 
specialAllowence = float(input("Enter your monhly allowence : ")) 
Bonuspercentage = float(input("Enter bonus percentage : ")) 

monthly_gross_salary = monthlySal + specialAllowence
annual_bonus = (monthly_gross_salary * 12 )*(Bonuspercentage/100)
annual_gross_salary = (monthly_gross_salary * 12 ) + annual_bonus

print('Employee id= ', emp_id)
print('Employee name= ', name)
print('Monthly gross salary= ', monthly_gross_salary)
print('Annual gross salary= ', annual_gross_salary)

print('%-6s %-15s %-20s %-20s' % ('Emp ID', 'Name', 'Monthly Gross Salary', 'Annual Gross Salary'))
print('-' * 80)
print('%-6d %-15s %-20.2f %-20.2f' % (emp_id, name, monthly_gross_salary, annual_gross_salary))
name = input("Enter employee name  : ")
emp_id = int(input("Enter employee id : "))
monthlySal = float(input("Enter your monhly salary : ")) 
specialAllowence = float(input("Enter your monhly allowence : ")) 
Bonuspercentage = float(input("Enter bonus percentage : ")) 

monthly_gross_salary = monthlySal + specialAllowence
annual_bonus = (monthly_gross_salary * 12 )*(Bonuspercentage/100)
annual_gross_salary = (monthly_gross_salary * 12 ) + annual_bonus

standard_deduction = 50000 
taxable_income = annual_gross_salary - standard_deduction
print(f"Taxable Income: ₹{taxable_income:,.2f}")  

print('-' *27)
print('%12s %s' % ('salary range', 'taxable_per'))
print('-' *27)
print('%7d - %-7d %3d%%'%(0,300000))
print('%7d - %-7d %3d%%'%(300001,600000,5))
print('%7d - %-7d %3d%%'%(600001,900000,10))
print('%7d - %-7d %3d%%'%(900001,1200000,15))
print('%7d - %-7d %3d%%'%(1200001,1500000,20))
print('%7d - %-7s %3d%%'%(1500001,'or more',30))
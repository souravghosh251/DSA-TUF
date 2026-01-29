name = input("Enter your name")
monthly_salary = float(input("Enter your monthly salary"))

yearly_salary = monthly_salary * 12
bonus = 1000
final_salary = yearly_salary + (yearly_salary * bonus / 100)

print("\n ---- Salary Details-----")
print("Name:", name)
print("Monthly Salary:", monthly_salary)
print("Yearly Salary:", yearly_salary)
print("Final Salary:", final_salary)
# Loan Checker

salary = float(input("Enter monthly salary: "))
experience = int(input("Enter years of experience : "))

if salary>50000 and experience>=3:
    print("Loan Approved")
elif salary<40000 and experience>2:
    print("Loan Approved but with conditions")
else:
    print("Loan Not Approved")

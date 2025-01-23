salary = float(input("Enter salary: "))
year = float(input('Enter year of service: '))

if year > 5:
    salary = salary + salary*.05

print(f'Total Salary: {salary}')
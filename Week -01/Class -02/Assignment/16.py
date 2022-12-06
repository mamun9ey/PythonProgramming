#16)write a program that accepts an employee's id ,total worked hours of a mounth and the amount he received per hour. Print the employee's id and salary of a particular mounth.
print("Input the Employees ID: ")
id=input()
print("\nInput the working hrs: ")
hour=int(input())
print("\nSalary amount/hr: ")
value=float(input())
salary = float(value * hour)
print(id,salary)


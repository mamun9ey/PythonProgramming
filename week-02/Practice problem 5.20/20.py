print("Enter Two Numbers: ", end="")
num1 = int(input())
num2 = int(input())

a = num1
b = num2
while b!=0:
    temp = b
    b = a%b
    a = temp

gcd = a
lcm = int((num1*num2)/gcd)

print("\nLCM (" + str(num1) + ", " + str(num2) + ") = ", lcm)
print("GCD (" + str(num1) + ", " + str(num2) + ") = ", gcd)
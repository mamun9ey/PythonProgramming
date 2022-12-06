#10)Write a program to compute the perimeter and area of a circle with a given radius

# Initialising the value of PI
PI = 3.14
# Getting input from user
R = float(input("Enter radius of the circle: "))

# Finding the area and perimeter of the circle
area = (PI*R*R)
perimeter = (2*PI*R)

# Printing the area and perimeter of the circle 
print("The area of circle is", area)
print("The perimeter of circle is", perimeter)
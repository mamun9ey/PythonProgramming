#11)write a program to find the thrid angle of a triangle if two angles are given
print("Enter two angles of triangle: ")
a = float(input())
b = float(input())
#Calculate the third angle

c = 180 - (a + b)

#Print the value of third angle
print("Third angle of the triangle = ", c)
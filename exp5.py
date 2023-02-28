"""
AUTHOR: Priya Babu

DATE: 28/02/2023

PROGRAM: Python Program to Solve Quadratic Equation
"""
import math
print("Enter the value a for x2")
a = int(input())
print("Enter the value a for x")
b = int(input())
print("Enter the value a for C")
c= int(input())
print("THe given quadratic equation is:")
print(a,"x^2","+",b,"x +",c)

d= b**2-4*a*c

if d>0:
    root1 = -b+((math.sqrt(d))/2*a)
    print("Root is",root1)
elif d<0:
     root2 = -b+((math.sqrt(d))/2*a)
     print("Root is",root2)
else:
     print("They are real root")
     




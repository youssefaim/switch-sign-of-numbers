#!/usr/bin/python3
# Input: Ask the user for 2 numbers
A = float(input("Enter the first number: "))
B = float(input("Enter the second number: "))
if (A > 0 and B > 0) or (A < 0 and B < 0) :
    C = A
    A = B
    B = C
else :
    C = A
    A = C + B
    B = C * B
print("The first number entered is now", A)
print("The second number entered is now", B)
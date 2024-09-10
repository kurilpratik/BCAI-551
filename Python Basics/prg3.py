# Write a Python function that takes two numbers as input and returns their greatest common divisor (GCD).

import math

def ret_gcd(a,b):
    return math.gcd(a,b)

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

gcd = ret_gcd(a,b)
print(gcd)


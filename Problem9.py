
# 9 - Newton's Method for Square Roots

import math
from decimal import *
getcontext().prec = 15

x = Decimal(input("Enter a number: "))
z = Decimal(input("Sqrt guess: "))

print("Math.sqrt(x): \t\t" + str(Decimal(math.sqrt(x)))) # Accurate sqrt

approximate = z - ((z*z - x) / (2 * z))
difference = 1
count = 1 # Calculation done once

while difference > 0.00000000001:
    z = approximate
    approximate = z - ((z*z - x) / (2 * z))
    difference = z - approximate
    count = count + 1

print("Newton's Method: \t" + str(approximate) + " (" + str(count) + " iterations)")
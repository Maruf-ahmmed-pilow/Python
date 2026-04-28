'''
The standard form of a quadratic equation is :
ax^2 + bx + c = 0

where a,b and c are real numbers and a != 0

The solutions of a quadratic equation is given by :

(-b+-(b^2 - 4ac)^0.5)/(2a)

'''

import math
a = float(input('Enter the coefficient a:'))
b = float(input('Enter the coefficient b:'))
c = float(input('Enter the coefficient c:'))

discriminant = b**2 -4*a*c

if discriminant > 0 :
    #two real and distinct roots
    root1 = (-b + math.sqrt(discriminant))/ (2*a)
    root2 = (-b - math.sqrt(discriminant))/ (2*a)
    print(f"Root1: {root1}")
    print(f"Root2: {root2}")

elif discriminant == 0:
    root = -b / (2*a)
    print(f"Root: {root}")

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Root1: {real_part} + {imaginary_part}i")
    print(f"Root2: {real_part} - {imaginary_part}i")


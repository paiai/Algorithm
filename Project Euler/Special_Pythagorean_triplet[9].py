"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
Answer: 31875000
"""

# a + b = 1000 - c

from math import sqrt 

def isINT(num):
    if int(num)==num:
        return True
    else:
        return False

for a in range(1, 500):
    for b in range(a+1, 500):
        c = sqrt(a**2 + b**2)
        if isINT(c) and (a+b+c == 1000):
            print(a, b, c, a + b + sqrt(a**2 + b**2))   # 200 375 425.0 1000.0
            print('a * b * c = ', a*b*c)                # a * b * c =  31875000.0

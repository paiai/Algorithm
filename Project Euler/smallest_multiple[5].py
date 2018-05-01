"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

=> Answer: 232792560
"""

"""
def GCD(M, N):
    while (N != 0):
        M, N = N, M % N
    return M

LCM = 1
for X in range(1, 21):
    LCM = (X * LCM)/GCD(X, LCM)
print(LCM)
"""

"""
#### 1
def isDivisible(number):
    for i in range(1, 20+1):
        if number % i != 0:
            return False
    return True

# 20 이후 숫자 증가시켜가면서 최소값을 찾는다
number = 21        
while True:
    if isDivisible(number):
        break
    number += 1
print(number)
"""

#### 2
def isDivisible(number):
    for i in range(1, 20+1):
        if number % i != 0:
            return False
    return True

# 20 이상 숫자 증가시켜가면서 최소값을 찾는다
number = 20        
while True:
    if isDivisible(number):
        break
    number += 20
print(number)
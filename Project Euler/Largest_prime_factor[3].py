"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

=> Answer: 6857
"""

from math import sqrt 

num = 13

result = []
value = 2
lastFactor = 1

# num 이 2의 배수인 경우 2로 나누어지지 않을 때까지 구한다.
if num % value == 0:
    num /= value
    lastFactor = value
    result.append(lastFactor)

    while num % value == 0:
        num /= value
    
value += 1 # value = 3

while value <= sqrt(num):
    if num % value == 0:
        num /= value 
        lastFactor = value
        result.append(lastFactor)
    
        while num % value == 0:
            num /= value


        print(num, value)
    value += 2

print(lastFactor)
print(result)
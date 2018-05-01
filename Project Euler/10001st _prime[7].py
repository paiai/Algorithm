"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

=> Answer: 104743
"""

array = [2]
number = 1
def isPrimeNumber(number):
    for i in range(len(array)):
        if (number % array[i] == 0):
            return False
    return True

while len(array) < 10001:
    number += 2
    if isPrimeNumber(number):
        array.append(number)
    
print(array[10000])
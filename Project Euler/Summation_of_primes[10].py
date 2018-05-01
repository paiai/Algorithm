"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922
"""

from math import sqrt

array = []
value = 2
num = 2000000
result = 0

def isPrime(number):
    for i in range(len(array)):
        if number % array[i] == 0:
            return False    
    return True

def isINT(number):
    if int(number) == number:
        return True
    return False

if num % 2 == 0:        # 짝수인지 확인, 짝수라면 2 외에 짝수인 소수는 없다.
    array.append(2)
    result += 2

for n in range(3, num, 2):
    if isINT(sqrt(n)):
        continue

    if isPrime(n):
        array.append(n)
        result += n

print(array)
#print(sum(array))
print(result)
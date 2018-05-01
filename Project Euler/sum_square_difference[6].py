"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

=> Answer: 25164150
"""


sum1 = sum([ n**2 for n in range(1, 100+1) ])
sum2 = sum([ n for n in range(1, 100+1) ])
mul1 = sum2**2

print(sum1)         # 338350
print(mul1)         # 25502500
print(mul1 - sum1)  # 25164150


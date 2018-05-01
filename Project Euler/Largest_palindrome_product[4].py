"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

=> Answer: 906609
"""

max_num = 0
for i in range(900, 1000):
    for j in range(900, 1000):
        num = str(i*j)
        if num == num[::-1]:    # num[::-1] 역순으로
            max_num = int(num)
 
print(max_num)
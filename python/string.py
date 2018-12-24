"""
aaabbcccccca

출력 예시: a3b2c6a1
"""

s = input()
result = s[0]
count = 1

for ch in s[1:]:
  if ch == result[-1]:
    count+=1
  else:
    result += str(count) + ch
    count = 1
    
result += str(count)

print(result)
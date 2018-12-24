#입력 예시: aaabbcccccca
#출력 예시: a3b2c6a1


#str = input()

s = 'aaabbcccccca'
count = 0
result = s[0]

for ch in s:
  if result[-1] == ch:
    count+=1
  else:
    result += str(count) + ch
    count = 1
result += str(count)    



# result = {}
# for ch in str:
#   if ch in result:
#     result[ch] += 1
#   else:
#     result[ch] = 1
    
print(result)
  
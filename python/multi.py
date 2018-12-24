print('1 :', eval('+'.join('*'.join(str(x)) for x in range(10, 1001))))

result = 0
for num in range(10,1001):
  sum = 1
  for j in str(num):
    sum *= int(j)
  
  result = result + sum  
    
print('2 :', result)

result = []
for x in range(10,1001):
  result.append(str(eval('*'.join(str(x)))))
  
print('3 :', eval('+'.join(result)))



#print(sum(eval('*'.join(str(x))) for x in range(10,1001)))    
#print(eval('+'.join('*'.join(str(x)) for x in range(10, 1001))))

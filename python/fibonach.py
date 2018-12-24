"""
예) 0, 1, 1, 2, 3, 5, 8, 13

인풋을 정수 n으로 받았을때, n 이하까지의 피보나치 수열을 출력하는 프로그램
"""
n = input()
array = [0,1]

def fibonach(n):
  i = 0
  while array[i] + array[i+1] <= int(n):
    array.append(array[i] + array[i+1])
    i+=1
    
fibonach(n)

print(array)


a=0;b=1
print('0', end='')
while b<=int(n):
    print(", {0}".format(int(b)), end='') # end='' 는 print 하고 줄바꿈 안 하도록
    a,b = b,a+b
print()
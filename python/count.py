count = { x:0 for x in range(0,10) }
count=[0 for x in range(0,10)]
#print(count)

for x in range(1,1000):
  for i in str(x):
    count[int(i)]+=1
    
print(count)
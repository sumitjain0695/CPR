import math
def dig_sum(n):
  s=0
  while(n>0):
    s+=n%10
    n=n/10
  return s

for _ in range(int(input())):
  n,d=map(int,input().split())
  t=[0]*(32)
  t[0]=n
  for i in range(16):
    t[(2*i)+1]=dig_sum(t[i])
    t[(2*i)+2]=t[i]+d
    print(t)
  m=min(t)
  i=t.index(m)
  print (m,int(math.log(i+1,2)))
    
    
  

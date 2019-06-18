from collections import Counter
for _ in range(int(input())):
    n,m=map(int,input().split())
    a1=[int(x) for x in input().split()]
    a2=[int(x) for x in input().split()]
    srtd=[]
    temp=[]
    d=dict(Counter(a1))
    print(d)
    for i in a2:
        print(i,d[i])
        print([i]*d[i])
        if i in d:
            srtd+=[i]*d[i]
            d[i]=0
    print(srtd)    
    
    for i in d:
        if d[i]>0:
            temp+=[i]*d[i]
    ans=srtd+sorted(temp)
    print(' '.join(str(x) for x in ans))
    
        
        
    

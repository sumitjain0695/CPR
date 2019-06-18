from collections import Counter
for _ in range(int(input())):
    n=map(int,input().split())
    a1=[int(x) for x in input().split()]
    d=dict(Counter(a1))
    ans=[]
    for i in d:
        ans.append([d[i],i])
    #ans=sorted(ans,reverse=True)
    #ans=sorted(ans,key=lambda x:x[1])
    ans.sort(key=lambda k:(k[0],-k[1]),reverse=True)
    #print(ans)
    a=[]
    for i in ans:
        a+=[i[1]]*i[0]
    print(' '.join(map(str,a)))    
        
        
    
        
    
    
        
        
    

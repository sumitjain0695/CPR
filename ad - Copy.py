for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    print(l)
    q=[]
    i=0
    j=0
    for i in range(len(l)-2,0,-1):
        if l[i]<l[i+1]:
            break
    if i==-1:
        print(-1)
    for j in range(i+1,len(l)):
        if l[j]<=l[i]:
            break
    print(i,j)    
    l[i],l[j-1]=l[j-1],l[i]
    l1=sorted(l[i+1:])
    d=l[:i+1]+l1
    print(''.join(map(str,d)))
        

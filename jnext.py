for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    i = len(l)-1
    while i>0 and l[i-1]>=l[i]:
        i-=1
    if i<=0:
        print(-1)
    j = len(l)-1
    while l[j] <= l[i-1]:
        j-=1
    l[i-1],l[j]=l[j],l[i-1]
    l[i:]=l[len(l)-1:i-1:-1]
    print (''.join(map(str,l)))

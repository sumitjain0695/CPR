for _ in range(int(input())):
    n,m=map(int,input().split())
    d={}
    for i in range(1,m+1):
        d[i] = -1
    for i in range(n):
        a,b=map(int,input().split())
        if d[a]<b:
            d[a]=b
    v=list(d.values())
    maximum=max(v)
    v.remove(maximum)
    max2=max(v)
    print(maximum+max2)

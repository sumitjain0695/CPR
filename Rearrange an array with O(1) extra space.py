while t:
    t-=1
    n=int(input())
    l=input().split()
    for i in range(n):
        print(l[int(l[i])],end=" ")
    print("")


    n=int(input())
    ar=input().split()
    for i in range(n):
        e=int(ar[int(ar[i])])%n
        ar[i]=e*n+int(ar[i])
    for i in range(n):
        r=ar[i]%n
        ar[i]=ar[i]-r
        print(ar[i]//n,end=" ")
    print()    

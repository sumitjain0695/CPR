n, k =map(int,input().split())
l = [int(x) for x in input().split()]
if n ==1:
    if k%2 ==0:
        print(l[0])
    else:
        print(-1)
if k == 1:
    print(l[1])
elif k < n:
    print(max(max(l[0:k-1]),l[k]))
elif k == n:
    print(max(l[:n-1]))
else:
    print(max(l[:n]))
     

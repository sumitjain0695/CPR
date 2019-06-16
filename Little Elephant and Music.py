for _ in range(int(input())):
    n = int(input())
    s = set()
    ls = []
    arr = []
    for i in range(n):
        b, l = map(int,input().split())
        ls.append([l,b])
    ans=0
    cnt=0
    ls.sort()
    for i in range(n):
        if ls[i][1] not in s:
            cnt+=1
            ans+=cnt*ls[i][0]
            s.add(ls[i][1])
        else:
            arr.append(ls[i][0])
    # for remaining        
    for i in range(len(arr)):
        ans+=cnt*arr[i]
    print(ans)

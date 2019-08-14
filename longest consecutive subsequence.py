for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    s = set() 
    ans=0
    for ele in arr: 
        s.add(ele) 
    for i in range(n): 
        if (arr[i]-1) not in s: 
            j=arr[i] 
            while(j in s): 
                j+=1
            ans=max(ans, j-arr[i]) 
    print(ans)

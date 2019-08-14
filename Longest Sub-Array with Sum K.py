for _ in range(int(input())):
    n ,k = map(int,input().split())
    arr = list(map(int,input().split()))
    s = 0
    maxlen = 0
    ht={}
    for i in range(n):
         s += arr[i]
         if s == k:
              maxlen = i+1
         if s not in ht:
              ht[s] = i
         if s-k in ht:
              idx = i-ht[s-k]
              if maxlen < idx:
                   maxlen = idx
    print(maxlen)               
    

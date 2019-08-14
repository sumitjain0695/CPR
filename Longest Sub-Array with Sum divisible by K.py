for _ in range(int(input())):
    n ,k = map(int,input().split())
    arr = list(map(int,input().split()))
    maxlen = 0
    mod_arr=[0]*n
    ht={}
    currsum=0
    for i in range(n):
        currsum +=arr[i]
        mod_arr[i] = ((currsum%k)+k)%k
        
    for i in range(n):
         if mod_arr[i] == 0:
              maxlen = i+1
         elif mod_arr[i] not in ht:
              ht[mod_arr[i]] = i
         else:
              idx = i-ht[mod_arr[i]]
              if maxlen < idx:
                   maxlen = idx
    print(maxlen)               
    

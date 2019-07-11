for _ in range(int(input())):
    k= int(input())
    n=int(input())
    arr = sorted([int(x) for x in input().split()])
    
    ans = arr[n-1] - arr[0]  
    small = arr[0] + k  
    big = arr[n-1] - k  
      
    if (small > big): 
        small, big = big, small  
    for i in range(1, n-1):
        subtract = arr[i] - k  
        add = arr[i] + k  
        if (subtract >= small or add <= big): 
            continue
        if (big - subtract <= add - small): 
            small = subtract  
        else: 
            big = add  
    print(min(ans, big - small))  

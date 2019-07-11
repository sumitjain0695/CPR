def findMinimum(arr,n,k):
    res = 0
    i=0
    while i<n:
        res += arr[i] 
        n = n-k 
        i+=1
    return res 

def findMaximum(arr, n, k):
    res = 0
    index = 0
    i=n-1
    while(i>=index):
            res += arr[i]  
            index += k 
            i -= 1
    return res

for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = sorted([int(x) for x in input().split()])
    print(findMinimum(arr, n, k),findMaximum(arr, n, k)) 



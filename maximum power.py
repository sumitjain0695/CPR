import sys 
def kthSmallest(arr, l, r, k): 
    if (k > 0 and k <= r - l + 1): 
        pos = partition(arr, l, r) 

        if (pos - l == k - 1): 
            return arr[pos] 
        if (pos - l > k - 1): 
            return kthSmallest(arr, l, pos - 1, k) 
        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)
    return sys.maxsize 
def partition(arr, l, r): 
    x = arr[r] 
    i = l 
    for j in range(l, r): 
        if (arr[j] <= x): 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
    arr[i], arr[r] = arr[r], arr[i] 
    return i 
def inc(l,n):
     for i in l:
          i+=n
     return l
def dec(l,n):
     for i in l:
          i-=n
     return l
for _ in range(int(input())):
     q = int(input())
     que = []
     for i in range(q):
          que.append(input())
     print(que)
     l = []
     length = 0
     for i in range(q):
          if que[i][0] == 'A':
               l.append(int(que[i][1:]))
               length +=1
          if que[i][0] == 'I':
               l = [(x+int(que[i][1:])) for x in l ]
          if que[i][0] == 'D':
               l = [(x-int(que[i][1:])) for x in l ]
          if que[i][0] == 'P':
               k = int(que[i][1:])
               #print('l is',l,length)
               m =length+1-k
               #print(m)
               print(kthSmallest(l, 0, length - 1, m))


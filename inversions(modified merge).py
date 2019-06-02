def merge(b,c):
    res=[]
    inv=0
    while b and c:
        if b[0]<=c[0]:
            res.append(b.pop(0))
        else:
            res.append(c.pop(0))
            inv+=len(b)
    res+= b or c
    return res,inv

def mergesort(l):
    if len(l)==1:
        return l,0
    mid=len(l)//2
    left,left_inv=mergesort(l[:mid])
    right,right_inv=mergesort(l[mid:])
    merged,merged_inv=merge(left,right)
    return merged,merged_inv+left_inv+right_inv
l=list(map(int,input().split()))
print(mergesort(l))

            

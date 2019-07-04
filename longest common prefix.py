def commonPref(str1, str2): 
    n1 = len(str1) 
    n2 = len(str2)
    res = "" 
    j = 0
    i = 0
    while i < n1 and j < n2:
        if str1[i] != str2[j]:
            break
        res += str1[i]
        i+=1
        j+=1
    if res ==0:  
        return -1
    return res
for _ in range(int(input())):
    a = map(int,input().split())
    l = [(x) for x in input().split()]
    max_l = max(l)
    min_l = min(l)
    print(commonPref(max_l,min_l))
    
    

for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    sl = sorted(l)
    ans = []
    for i in range(n):
        for j in range(n-1,-1,-1):
            if l[i] == sl[0]:
                ans.append(0)
                sl.pop(0)
                break
            if l[i] < l[j]:
                continue
            if l[i] > l[j]:
                #print('j-i=',j-i)
                if j-i >0:
                    ans.append(j-i)
                    break
                else:
                    ans.append(0)
                    break
    print(*ans)            
                

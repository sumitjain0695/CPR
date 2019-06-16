from collections import defaultdict
for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    dic = defaultdict(list)
    ans = 0
    for i in range(n):
        s,f,c = [int(x) for x in input().split()]
        dic[c].append([s,f])
    for i in dic:
        dic[i].sort()
        #print('dic[i] is',dic[i])
        p = [dic[i][0]]
        #print('p is',p)
        for y in (dic[i][1:]):
            #print('y is',y)
            if y[1] < p[-1][1]:
                #print('y[1] is < p[-1][1]')
                p.pop()
                p.append(y)
            elif y[0] >= p[-1][1]:
                #print('y[0] is >= p[-1][1]')
                p.append(y)
        ans += len(p)
    print(ans)	

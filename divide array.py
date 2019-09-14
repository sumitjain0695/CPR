n = int(input())
l = ([int(x) for x in input().split()])
l.sort()
set1 = set(l)
s2 = set()
left = []
rem = n//2 - len(set1)
if rem>0:
    print(rem)
    l = l[:n - rem]
    d = dict.fromkeys()
    i = 1
    while rem > 0:
        if i not in set1:
            s2.add(i)
            #set1.remove(i)
            rem-=1
        else:
            s2.add(i)
            set1.remove(i)
        i+=1    
    left = list(s2)
    for i in set1:
        left.append(i)
    left.sort()

    for i in left:
        try:
            l.remove(i)
        except:
            continue
    right = l
    print(*left+right)

else:
    print(0)
    print(*l)



        



    
 

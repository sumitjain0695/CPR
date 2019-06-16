for _ in range(int(input())):
    n,k=map(int,input().split())
    c=[]
    for j in range(n):
        d,e,f=map(int,input().split())
        c.append([e,d,f])
    c=sorted(c)
    #print(c)
    cnt=0
    m={}
    for i in c:
        #print('i is',i)
        if i[2] not in m:
            #print('not in')
            m[i[2]]=i[0]
            cnt+=1
        elif m[i[2]]<=i[1]:
            #print('m[i[2]]<=i[1] or',m[i[2]],'<=',i[1])
            m[i[2]]=i[0]
            #print('set',m[i[2]],'=',i[0])
            cnt+=1
    print(cnt)

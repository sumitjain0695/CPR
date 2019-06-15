for i in range(int(input())):
    n=int(input())
    threads=[]
    
    for i in range(n):
        threads.append(list(map(int,input().split())))
    stack=list(map(int, input().split()))
    size=[]
    
    for s in range(len(threads)) :
        size.append(threads[s][0])
        
    for j in stack:
        for k in range(n):
            if size[k]!=0:
                #print('not empty')
                if j==threads[k][size[k]]:
                    #print('last matched',j)
                    size[k]-=1
    if size.count(0)==n:
        print("Yes")
    else:
        print("No")

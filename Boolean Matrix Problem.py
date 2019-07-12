for _ in range(int(input())):
    r,c = map(int,input().split())
    row = [0]*r
    col = [0]*c
    mat = []
    
    for i in range(r):
        mat.append([int(x) for x in input().split()])
        
    for i in range(r):
        for j in range(c) : 
            if mat[i][j] == 1: 
                row[i] = 1
                col[j] = 1
                
    for i in range(r) : 
        for j in range(c): 
            if row[i] == 1 or col[j] == 1: 
                mat[i][j] = 1
                
    for i in range(r):
        print(*mat[i])

for _ in range(int(input())):
    
    m,s=map(int,input().split())
    res = [0] * m 
    if (s == 0) :
        if(m == 1) : 
            print(0)  
    
    for i in range(0, m) : 
        if (s >= 9) : 
            res[i] = 9
            s = s - 9
        else : 
            res[i] = s 
            s = 0
    for i in range(0, m) : 
        print(res[i],end = "")
    print()    

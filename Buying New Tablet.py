for _ in range(int(input())):
    n,b=map(int,input().split())
    ar=[]
    prices=[]
    for i in range(n):
        w,h,p=map(int,input().split())
        ar.append(w*h)
        prices.append(p)
    #print(ar)
    #print(prices)    
    prices=[0 if x>b else x for x in prices]
    indices = [i for i, x in enumerate(prices) if x==0]
    #print(indices)
    for i in indices:
        ar[i]=0
    #print('  ',ar)
    #print('  ',prices)    
    if set(prices)=={0}:
        print('no tablet')
    else:
        print(max(ar))
        
        
        
       
            
            

        
    
        
    
    
        
    
        
    
    

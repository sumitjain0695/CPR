from collections import Counter
def factors(n):
    return [x for x in range(1, n+1) if n % x == 0]
def spread(addn,factor):
    div=addn//factor
    return [div for x in range(factor)]
for _ in range(int(input())):
    l=input()
    l=list(l)
    ans=[]
    l1=sorted(tuple(Counter(l).values()),reverse=True)
    #print(l1)
    sums=sum(l1)
    length=len(l1)
    fctrs=factors(sums)
    for factor in fctrs:
        #print('factor is',factor)
        sprd=sums//factor
        if length>=factor:
            lbase=list(l1)
            for j in range(factor):
                lbase[j]=lbase[j]-sprd
            #print('step list is',lbase)     
            ans.append(sum(map(abs,lbase))//2)
        else:
            spreaded=spread(sums,factor)
            if len(spreaded)<=26:
                for j in range(length):
                    spreaded[j]=spreaded[j]-l1[j]
                #print('spread exceeded list l1 so step list is',spreaded)    
                ans.append(sum(map(abs,spreaded))//2)    
    #print('possible answers',ans)
    print(min(ans))
            
            
            
        
    
            
            

        
    
        
    
    
        
    
        
    
    

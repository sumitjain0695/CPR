#Moore’s Voting Algorithm

def findcan(l):
    maj_ind=0
    c=1
    for i in range(len(l)):
        if l[maj_ind]==l[i]:
            c+=1
        else:
            c-=1
        if c==0:
            maj_ind=i
            c=1
    return l[maj_ind]

def ismaj(l,cand):
    c=0
    for i in range(len(l)):
        if l[i]==cand:
            c+=1
    if c>len(l)/2:
        return True
    else:
        return False

                
            
        
        
    
    

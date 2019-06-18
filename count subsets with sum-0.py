l=[int(x) for x in input().split()]
ll=[0,l[0]]
s=l[0]
cnt=0
for i in range(1,len(l)):
    s+=l[i]
    ll.append(s)
d={}
for i in ll:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
#print(d)        
for i in d:
    val=d.get(i)
    #print('i is',i,'and -',val)
    if val>1:
        cnt+=val*(val-1)/2
        #print('cnt is',cnt)
print(cnt)        

    
    
    


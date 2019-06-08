while True:
    l=[int(x) for x in input().split()]
    if l[0]==0:
        break
    st=[]
    max_ar=0
    i=0
    n=len(l)
    while i<n:
        if st==[] or l[st[-1]]<=l[i]:
            print(i,'appended in st')
            st.append(i)
            i+=1
        else:
            print(st[-1],'popped from st')
            top=st.pop()
            
            if st==[]:
                print('st is empty')
                ar=l[top]*i
            else:
                ar=l[top]*(i-st[-1]-1)
            max_ar=max(max_ar,ar)
    while st!=[]:
        top=st.pop()
        if st==[]:
                ar=l[top]*i
        else:
            ar=l[top]*(i-st[-1]-1)
        max_ar=max(max_ar,ar)
    print(max_ar)    
    
                
            
    
 

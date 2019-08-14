
for _ in range(int(input())):
    string = input()
    n = len(string) 
    st = [] 
    st.append(-1) 
    result = 0
    for i in range(n): 
        if string[i] == '(': 
            st.append(i) 
        else:
            st.pop() 
            if len(st) != 0: 
                result = max(result, i - st[len(st)-1]) 
            else: 
                st.append(i) 
  
    print(result)

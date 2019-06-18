def countSubarrWithEqualZeroAndOne (arr): 
    um = dict() 
    curr_sum = 0
    for i in range(len(arr)): 
        curr_sum += (-1 if (arr[i] == 0) else arr[i]) 
        if um.get(curr_sum): 
            um[curr_sum]+=1
        else: 
            um[curr_sum]=1
    count = 0
    for itr in um: 
        #print('itr is',itr)
        #print('um[itr] is',um[itr])
        if um[itr] > 1:
            #print('count added',((um[itr] * int(um[itr] - 1)) / 2))
            count += ((um[itr] * int(um[itr] - 1)) / 2) 
    if um.get(0):
        #print('didnt understand',um.get(0))
        #print('here',um[0],'is added')
        count += um[0] 
    return print( int(count) )

arr = [int(x) for x in input().split()] 
countSubarrWithEqualZeroAndOne(arr)


T=int(input())
for _ in range(T):
    
    print('Q',0,0)
    d1=int(input())
    if d1==0:
        print('Q',1000000000,0)
        d2=int(input())
        print('Q',0,1000000000)
        d3=int(input())
        xl=0
        yl=0
        xu=1000000000-d2
        yu=1000000000-d3
    else:    
        print('Q',d1,0)
        d2=int(input())
        print('Q',0,d1)
        d3=int(input())
        

        print('Q',3*d1-d2-d3,0)
        d4=int(input())

        print('Q',0,3*d1-d2-d3)
        d5=int(input())

        print('Q',0,d4//2)
        xl=int(input())

        print('Q',d5//2,0)
        yl=int(input())

        yu=xl+d1-d3

        xu=yl+d1-d2

    print('A',xl,yl,xu,yu)
        
    inp=int(input())
    if inp<0:
        break

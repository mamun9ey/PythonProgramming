for i in range(int(input())):
    x,y=map(int,input().split())
    
    if x>y:
        print('NO')
    
    elif y>x+200:
        print('No')
    else:
        print('YES')
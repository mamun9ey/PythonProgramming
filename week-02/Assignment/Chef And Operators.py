n = input()
s = int(n)
for i in range(s):
    a,b = map(int,input().split())
    if(a>b):
        print(">")
    elif(a<b):
        print("<")
    else:
        print("=")

        
        

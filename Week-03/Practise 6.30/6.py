#Python Program to make Fibonacci series using list

n=int(input("Enter the number terms: "))
f=0                                         
sum=1                                        
if n<=0:
    print("The fibonacci series is: ",f)
else:
    print(f,sum,end=" ")
    for x in range(2,n):
        next=f+sum                          
        print(next,end=" ")
        f=sum
        sum=next
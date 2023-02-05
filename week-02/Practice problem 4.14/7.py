#Write a program to check whether a charcter is alphabet or not 
c=input()
if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <='Z')):
    print(c,"is an alphabet.")
else:
 print(c," is not an alphabet.")
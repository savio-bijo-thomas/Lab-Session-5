"""Author:Savio Bijo Thomas
   Date:29-10-24
   Purpose:To print n prime numbers"""

limit=int(input("enter the limit:"))
for i in range(2,limit+1):
    isprime = True
    for j in range(2,i//2+1):
        if i%j==0:
            isprime=False
            break
    if isprime:
        print(i)




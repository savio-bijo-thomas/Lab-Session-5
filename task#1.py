"""Author:Savio Bijo Thomas
   Date:29-10-24
   Purpose:to check whether the given number is prime or not"""

number=int(input("enter the number:"))
isprime=True
for i in range(2,number//2+1):
    if number%i==0 :
        isprime=False
if isprime:
    print(f"the number {number} is prime.")
else:
    print(f"the given number {number} is not prime.")
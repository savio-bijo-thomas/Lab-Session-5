"""Author:Savio Bijo Thomas
   Date:29-10-24
   Purpose:To find the number of vowels in a string"""

string=input("enter the string:")
vowels="aeiouAEIOU"
vowels_count=0
consonants =0
for char in string:
    if char in vowels:
        vowels_count+=1
    else:
        consonants+=1
print("number of vowels in",string,"=",vowels_count)
print("the number of consonants ",string,"=",consonants)
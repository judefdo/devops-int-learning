#How do you check if two strings are anagrams of each other?
import re

string1="Dormitory"
string2="dirty room"

tstr1 =sorted(string1.replace(" ","").lower())
tstr2 =sorted(string2.replace(" ","").lower())

if tstr1 == tstr2 :
    print("May be")
    print(tstr2, tstr1)
else:
    print("It is not an anagram") 


# extract a Upper character 
res = [ char for char in string1 if char.isupper() ]
print(str(res))

# Using filter
res = list(filter(lambda char: char.isupper(),string1))
print(str(res))
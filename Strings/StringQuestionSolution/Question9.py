#How do you count a number of vowels and consonants in a given string?
vowel=['a','e','i','o','u']
string1="Iamangoodguy"

diccount=0
conscount=0

res=list(map(lambda x: x in vowel, string1.lower())).count(True)

print(res)
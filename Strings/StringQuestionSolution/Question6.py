#How do you check if a string contains only digits? (solution)

string1="34567A"

import re


patt=re.compile('^[0-9]+$')
value=patt.match(string1)
print(value)

if value != None :
        print("String has all digit")
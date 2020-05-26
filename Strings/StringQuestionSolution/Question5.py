from functools import reduce
string1="Thisisastring"
res= dict(map(lambda x: (x,string1.count(x)),string1.lower()))
print(str(res))
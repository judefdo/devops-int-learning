# How do you print the first non-repeated character from a string?
string1="GeeksofGeeks"
res=dict(map(lambda x: (x,string1.count(x)),string1))
for k,v in res.items():
    if v == 1:
        print(k)
#        exit(0)
temp=string1
res1 = next(filter(lambda x: (temp.count(x) == 1)   , string1 ))
print(str(res1))

# Remove dupliate character from a string
res1 = set(map(lambda x:x,string1))
print(str(res1))
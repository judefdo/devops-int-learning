from collections import Counter

string1="abcbaba"
string2=string1.split()
res=[]
count=0
for i in range(len(string1)):
    res=["".join(string1[i:j]) for j in range(i,len(string1))]
    for item in res:
        print(item[::-1], res.count(item[::-1]))
        if len(item) == 1 or res.count(item[::-1]) > 0 :
            count += 1
    print(res)
print(count)
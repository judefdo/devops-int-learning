# How do you find all the permutations of a string? (solution)

#string1 = "I am great"
string1="abcd"
newstr=string1.replace(" ","")
print(newstr)
res=[]
for k, i in enumerate(newstr):
    count=i
    for k1, j in enumerate(newstr[k+1:]):
        count += j
        res.append(count)
print(str(res))    

from functools import reduce
newlist=newstr.split()
print(type(newlist))
res = list(reduce((lambda x,y: str(x)+str(y)),newlist))
print(str(res))


from itertools import permutations

res = [''.join(p) for p in permutations(newstr)]
print(str(res))

def permuta(string1, step=0):
    print(string1, step)
    if step == len(string1):
        print("".join(string1))
    for i in range(step, len(string1)):
        string_copy = [ c for c in string1 ]
        string_copy[step],string_copy[i]=string_copy[i],string_copy[step]
       
        permuta(string_copy,step + 1)

print(permuta('abcd'))
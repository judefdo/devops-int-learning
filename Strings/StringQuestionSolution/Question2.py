# How do you print duplicate characters from a string?

strvalue=" This a string"
a=set()

# First method to use count    
for i in strvalue:
    if strvalue.count(i) > 1:
        a.add(i)
    print (i)

print (a)

# Without using any python methods

dup={}

for i in strvalue:
    if i in dup:
        dup[i] += 1
    else:
        dup[i] = 1
print("Second method")
for key,value in dup.items():
    if value > 1:
        print(key,end = " ")
       
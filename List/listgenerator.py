def double(L):
    for x in L:
        yield x*2

eggs = double([2,4,6,8])
print(type(eggs))
print(*eggs)
egglist = list(double([3,6,9,12]))
print(egglist)

# The above is a generator comprehension , it return output in object or to return the 
# the value in list we use the list(double([....]))

eggs=(x*2 for x in [4,6,7,8])
print(*eggs)
eggslist=[x*2 for x in [5,7,7,2]]
print(eggslist)
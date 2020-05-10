def bs(a):             # a = name of list
    b=len(a)-1         # minus 1 because we always compare 2 adjacent values
                             
    for x in range(b):
        print(x)
        for y in range(b-x):
            if a[y]>a[y+1]:
                print(",,,,,",a[y],a[y+1])
                a[y],a[y+1]=a[y+1],a[y]
                print(a[y],a[y+1])
    return a
a=[32,5,3,6,7,54,87]
bs(a)
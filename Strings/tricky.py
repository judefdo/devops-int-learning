squares=[]
for x in range(5):
    squares.append(lambda: x**2)
    print(x)
print(str(squares))    
print(type(squares))
print(squares[2]())
print(squares[4]())

a=True
print(('A','B')[a == True])


# Reduce example

product = 1
list = [1,2,3,4]
for num in list:
    product = product * num
print(product)
# in reduce format
from functools import reduce
product1 = reduce((lambda x,y: x*y),list)
print(product1)


# Map example

items = [1,2,3,4]
squared = list(map(lambda x: x**2,items))

def multiply(x):
    return (x*x)

def add(x):
    return(x+x)

funcs = [multiply,add]
for i in range(5):
    value = list(map(lambda x: x(i),funcs))
    print(value)

# Filter example
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

#

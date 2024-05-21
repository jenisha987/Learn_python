#--Lambda Function--


double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x, y: (x + y)/2

print(double(5))
print(cube(5))
print(avg(3,5))

def appl(fx, value):
    return 6 + fx(value)
# print(appl(cube, 2)) #normal way
print(appl(lambda x: x*x*x, 2)) #using lambda function




#--MAP, Filter, Reduce--
# MAP
def cube(x):
    return x * x* x
print(cube(2))
l = [1,2,3,4,5,6]
# newl = list(map(cube, l))
newl = list(map(lambda x: x * x * x, l)) #sabai list ko lai directly function apply hunxa instead of using loop
print(newl)

# # FILTER --returns either true or false, true wala lai print
def filter_function(a):
    return a > 2 #a > 2 (true) wala elements lai matra return garera dinxa
newnewl = list(filter(filter_function, l))
print(newnewl)

#REDUCE
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers )
print(sum)
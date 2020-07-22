from functools import reduce

a = reduce(lambda x,y : x+y,[20,40,60,70])
print(a)
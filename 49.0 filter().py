a = list(filter(lambda x : x %2 == 0 , [x for x in range(10)]))
print(a)

a = [x for x in range(100) if x % 2 == 0]
print(a)

def asalmi(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


print(asalmi(31))

a = filter(asalmi,[x for x in range(100)])
print(list(a))
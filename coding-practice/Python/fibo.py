#n = int(input())
def fibnoacii(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnoacii(n-1) + fibnoacii(n-2)
print(fibnoacii(10))
# fibnoacii(n)   
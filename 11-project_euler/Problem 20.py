


def factorial(n):
    if n==1:
        return(1)
    return((n*factorial(n-1)))

def sum_of_digits(x):
    sum = 0
    while True:
        x,b=divmod(x,10)
        sum+=b
        if x==0:
            return(sum)

print(sum_of_digits(factorial(100)))


# 更简洁的方法

from functools import reduce
print(sum(int(i) for i in str(reduce(lambda x,y:x*y,range(1,101)))))



from operator import mul
print(sum(int(i) for i in str(reduce(mul,range(1,101)))))

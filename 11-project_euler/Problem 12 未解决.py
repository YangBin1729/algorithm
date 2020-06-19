# import math
# def factor(n):
#     results=[1,n]
#     for i in range(2,int(math.sqrt(n))):
#         if n%i==0:
#             results.extend([i,n//i])
#     return(results)
#
#
# print(len(factor(500000000*1000000001)))


def triangle_num(n):
    return int(n*(n+1)/2)

import math
def divisors(num):
    n = 2
    mid = math.ceil(math.sqrt(num))
    for i in range(2, mid):
        a, b = divmod(num, i)
        if b == 0:
             n += 2
    return n

i = 100000
num = triangle_num(i)
n = divisors(num)
print(i, num, n)

# while True:
#     i = 8
#     num = triangle_num(i)
#     n = divisors(num)
#     if n > 500:
#         print(i, num, n)
#         break
#     else:
#         i += 1

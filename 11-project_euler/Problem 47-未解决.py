import csv
prime_file=open('prime_list.csv','r')
prime_list=list(csv.reader(prime_file))[0]
prime_file.close()

from math import sqrt


def prime_factors(n):
    results = []
    for i in prime_list:
        if int(i) < n and n % int(i) == 0:
            results.append(int(i))
    return results


limit = 100
factors = [0]*limit
count = 0

for i in range(2, limit):
    if factors[i] == 0:
        for j in range(2*i, limit, i):
            factors[j] += 1
    print(factors)

# 为什么这样计算得到的 质因子 个数是正确的？？？？？？？
# 素数筛:如果本身是素数，那只有一个素因子；当i*prime[j] 时，如果 i 能整除prime[j]，
# 那么素因子个数等于i的素因子个数；如果不能整除，加一即可？？？？？？

goal = [4]*4
for i in range(2, limit):
    if factors[i:i+4] == goal:
        print(i)
        break




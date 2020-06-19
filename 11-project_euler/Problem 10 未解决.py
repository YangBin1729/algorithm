from math import sqrt


def is_prime(n):
    for i in range(2,int(sqrt(n))):
        if n% i == 0:
            return False
    return True

print(is_prime(33))

limit = 2000000
results = 17
i = 11
while i < limit:
    tmp = str(i)
    if tmp.endswith('5') or sum(int(a) for a in tmp) % 3 == 0:
        i += 2
        break
    if is_prime(i):
        results += i

print(results)

# 更合理的解法

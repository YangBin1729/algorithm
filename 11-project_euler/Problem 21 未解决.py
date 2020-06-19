import math


def proper_divisors(n):
    results=[1]
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            results.append(i)
            results.append(n//i)
    return(sum(results))

print(proper_divisors(220))
print(proper_divisors(284))

for i in range(3,10000):
    for j in range(3,10000):
        if proper_divisors(i) == j and proper_divisors(j) == i:
            if i!=j:print(i,j)


220+284+1184+1210+2620+2924+5020+5564+6232+6368
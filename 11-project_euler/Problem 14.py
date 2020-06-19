# 较愚蠢的解法
"""
def collatz(n):
    i=1
    num=n
    while True:
        n=n//2 if n%2==0 else 3*n+1
        i+=1
        if n==1:
            break
    return(i,num)

print('the longest chain,the starting number',max([collatz(n) for n in range(2,1000000)]))
"""

# 快速、简洁
def collatz(n):
    return(n//2 if n%2==0 else 3*n+1)

def distance(n,cache={1:1}):
    if n not in cache:
        cache[n]=distance(collatz(n))+1
    return(cache[n])

print(max(range(1,1000000),key=distance))
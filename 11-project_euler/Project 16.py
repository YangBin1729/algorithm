"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""

def digit_sum(n):
    x=[6,1]
    for i in range(4,n):
        x = [2 * i for i in x]
        for i in range(len(x)-1):
            if x[i] >= 10:
                x[i] -= 10
                x[i+1] += 1
            if x[-1]>=10:
                x[-1]-=10
                x.append(1)
    return(x)



## 更好的答案：
a=2**1000
sum=0
while a>0:
    k=a%10
    sum+=k
    a=a//10
print(sum)
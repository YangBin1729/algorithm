"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


nums=range(1,21)
def common_div(a,b):
    tmp=min(a,b)
    for i in range(tmp,0,-1):
        if a % i == 0 and b % i == 0:
            return(i)

sum=1
for num in nums[::-1]:
    num/=common_div(num,sum)
    sum*=num
print(sum)


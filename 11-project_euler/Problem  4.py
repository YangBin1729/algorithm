"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


# 比较蠢的方法：

import copy
def is_palindromic(num):
    tmp=list(repr(num))
    tmp_reverse=copy.copy(tmp)
    tmp_reverse.reverse()
    if tmp==tmp_reverse:
        return(True)
    return(False)

states=True

def largest_palindrom():
    results=[]
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            num=i*j
            if is_palindromic(num):
                results.append(num)
    return(max(results))


# 简洁：
max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y)==str(x*y)[::-1]])

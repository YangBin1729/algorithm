"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""
import numpy as np
def sum_square_difference(n):
    tmp=np.array(range(1,n+1))
    return(np.sum(tmp)**2-np.sum(tmp**2))

print(sum_square_difference(10))
print(sum_square_difference(100))
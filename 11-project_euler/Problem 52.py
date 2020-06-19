# 愚蠢的解法

def is_same_digits(x):
    n=[2,3,4,5,6]
    cmp_0=set(str(x))

    for i in n:
        cmp_n=set(str(i*x))
        if cmp_n!=cmp_0:
            return(False)

    return(True)

"""
for n in range(2,20):
    for i in range(10**n,10**(n+1)//6):
        if is_same_digits(i):
            print(i)
"""

print(is_same_digits(125874))

last_digits={0:['0'],
             1:['2','3','4','5','6'],
             2:['4','6','8','0'],
             3:['6','9','2','5','8'],
             4:['8','2','6','0'],
             5:['0'],
             6:['2','8','4','0'],
             7:['4','1','8','5','2'],
             8:['6','4','2','0'],
             9:['4','7','6','5']}

def is_permuted(num):
    tmp=set(str(num))
    ii=num%10
    if set(last_digits[ii]).issubset(tmp):
        if is_same_digits(num):
            return(True)
    return(False)



for n in range(2,30):
    print('10^%d~10^%d'%(n,n+1))
    print([num for num in range(10**n,10**(n+1)//6) if is_permuted(num)])

# 1.末尾数字部分决定了整个数据序列
# 2.首位数字必须为1
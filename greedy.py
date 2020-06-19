__author__ = 'yangbin1729'

"""
算法思想：贪心、分治、回溯、动态规划

贪心算法：
-->解决最优化问题
-->分解成一系列步骤，类似树的分叉过程
-->每个步骤，又有多个选择
-->每一步选择当时最佳的选择，即局部最优
-->当前面的步骤会影响到后续的选择时，就不能保证最终结果是全局最优。
"""


# 一、活动选择问题：n 个活动，各自的起始时间，可以选择出的时间不冲突的活动的最大数量
def printMaxActivities(s, f):
    """
    :param s: 起始时间列表
    :param f: 终止时间列表，已排序
    :return:
    """
    n = len(f)
    
    i = 0
    print(i)
    
    for j in range(n):
        if s[j] >= f[i]:
            print(j)
            i = j


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f)

# 二、埃及分数，分子为 1 的分数：任何分数都可以表示成多个埃及分数之和
# TODO
import math


def egyptianFraction(nr, dr):
    """
    :param nr: 分子
    :param dr: 分母
    :return:
    """
    print("The Egyptian Fraction Representation of {0}/{1} is".format(nr, dr),
          end='\n')
    
    ef = []  # 储存埃及分数列表的分母
    
    while nr != 0:
        x = math.ceil(dr / nr)
        
        ef.append(x)
        
        nr = x * nr - dr
        dr = dr * x
    
    print(" + ".join([f"1/{i}" for i in ef]))


egyptianFraction(6, 14)


# 三、背包问题：n 件物品，价值-重量，总容量 W 的背包，可以放的最大价值的物品，物品可以拆分
class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt
    
    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapSack:
    @staticmethod
    def getMaxValue(wt, val, capacity):
        
        # 物品对象组成的列表，并按 价值/重量 比进行排序
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
        iVal.sort(reverse=True)  # 优先选择 价值/重量 比大的物品 --> 贪心策略
        
        totalVal = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalVal += curVal
            else:
                fraction = capacity / curWt
                totalVal += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalVal


def test_knapsack():
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50
    
    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)


# 四、最佳工作序列：一系列可以单位时间完成的工作，获利-deadline，选择获利最多的工作序列

def printJobScheduling(arr, t):
    # TODO
    pass


arr = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27], ['d', 1, 25], ['e', 3, 15]]

print("Following is maximum profit sequence of jobs")
printJobScheduling(arr, 3)
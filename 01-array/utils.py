from .dynamicArray import DynamicArray

"""列表长度与底层数组大小的关系
当列表长度与底层数组的大小相同时，再增加元素，底层数组大小会变大(动态数组算法)"""

import sys
import time

data = []


def compute_size(data):
    for k in range(30):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length:{0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(k)


def compute_average(n):
    data = []
    start = time.perf_counter_ns()
    for k in range(n):
        data.append(None)
    end = time.perf_counter_ns()
    return (end - start) / n


if __name__ == '__main__':
    print('测试 Python 列表大小')
    compute_size(data)
    print('=' * 80)
    
    print('测试自定义动态数组的大小')
    data = DynamicArray()
    compute_size(data)
    print('=' * 80)
    
    for i in range(1, 8):
        n = 10 ** i
        print('{} 次操作平均耗时 {}'.format(n, compute_average(n)))
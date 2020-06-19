__author__ = 'yangbin1729'


# 一、比较类排序
# 1. 插入排序：O(N^2)
# curr 元素左侧已排序，从右向左扫描 curr 左侧元素，找到相应位置插入 curr 元素
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        curr = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > curr:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = curr
    return nums


# 2. 选择排序：O(N^2)
# 每次找到最小值，然后放在待排序数组的起始位置
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


# 3. 冒泡排序：O(N^2)
# 比较相邻元素，第一个比第二个大，就交换；每一次遍历，最大值就移动到了最右边
def bubble_sort(nums):
    n = len(nums)
    for _ in range(1, n):
        for j in range(n - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 4. 希尔排序 shell sort：O(N^1.3)
# TOGRASP： 待理解
# 希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。
def shell_sort(nums):
    import math
    gap = 1
    while gap < len(nums) / 3:
        gap = gap * 3 + 1  # 1 4 13  # 4 13  40
    while gap > 0:
        for i in range(gap, len(nums)):
            tmp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > tmp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = tmp
        gap = math.floor(gap / 3)
    return nums


# 5. 快速排序：O(N*logN)
# 数组中取标杆 pivot，将小元素放 pivot 左边，大元素放右侧；然后递归的分别对左、右两部分快排
def partition(nums, left, r):
    pivot = nums[left]
    i = left + 1  # KEY： i-left 表示小于等于 pivot 元素的个数
    for j in range(left + 1, r):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[left], nums[i - 1] = nums[i - 1], nums[left]
    return i - 1


def quick_sort(nums, l, r):
    if l >= r:
        return
    j = partition(nums, l, r)
    quick_sort(nums, l, j)
    quick_sort(nums, j + 1, r)
    return nums


# 6. 归并排序：O(N*logN)
def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):  # KEY：关键的判断逻辑！！！
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1
    # # 另一种方案：
    # k = 0
    # while i < len(s1) and j < len(s2):
    #     if s1[i] < s2[j]:
    #         s[k] = s1[i]
    #         i += 1
    #     else:
    #         s[k] = s2[j]
    #         j += 1
    #     k += 1
    # if i < len(s1):
    #     s[k:] = s1[i:]
    # if j < len(s2):
    #     s[k:] = s2[j:]
    return s


def merge_sort(s):
    if len(s) < 2:
        return s
    mid = len(s) // 2
    s1 = merge_sort(s[:mid])
    s2 = merge_sort(s[mid:])
    return merge(s1, s2, s)


# TODO: 堆的实现
# 7. 堆排序：O(N*logN)
# 利用堆这种数据结构，堆为二叉树，其每个父节点的值都小于等于其子节点，数组表示为 h[k]<=h[2k+1]、h[k]<=h[2k+2]
# heappop 弹出堆中最小值
from heapq import heappush, heappop


def heap_sort(nums):
    h = []
    for num in nums:
        heappush(h, num)
    return [heappop(h) for _ in range(len(nums))]


# 二、非比较排序：主要用于整数序列的排序
# 8. 计数排序：O(N+k)
# 下述解法：待排序数组 nums 必须为正整数；求得 nums 最大值 max_num，然后统计从 0~max_num 每个值的个数
def counting_sort(nums):
    max_num = max(nums)  # O(N) 时间可以完成
    bucket = [0] * (max_num + 1)
    for i in range(len(nums)):
        bucket[nums[i]] += 1
    
    sortedIndex = 0
    for j in range(max_num + 1):
        while bucket[j] > 0:
            nums[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return nums


# 9. 桶排序：O(N+k)

# 桶排序是计数排序的升级版，利用函数的映射关系，算法效率的关键在于这个函数的设计。
# 工作原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序。
def bucket_sort(nums):
    min_, max_ = min(nums), max(nums)
    
    bucket_count = (max_ - min_) // 5 + 1  # 默认每个桶的容量为 5
    buckets = [[] for i in range(bucket_count)]
    
    for num in nums:
        ind = (num - min_) // 5  # 将每个数映射到特定的桶中，每个桶有顺序
        buckets[ind].append(num)
    
    res = []
    for buck in buckets:
        if bool(buck):
            res.extend(insertion_sort(buck))  # 对每个桶中的数插入排序
    return res


# 10. 基数排序（Radix Sort)  # 按个位数先排序，然后收集；再按百位数排序，然后再收集；依次类推，直到最高位


def radix_sort(nums):
    digit, max_digit = 0, 1
    max_value = max(nums)
    while 10 ** max_digit < max_value:
        max_digit += 1
    
    while digit < max_digit:
        tmp = [[] for i in range(10)]
        for i in nums:
            t = int((i / 10 ** digit) % 10)  # 依次求个位、十位、百位...
            tmp[t].append(i)
        
        coll = []
        for bucket in tmp:
            for i in bucket:
                coll.append(i)
        
        nums = coll
        digit += 1
    return nums


def radix_sort2(nums):
    radix, max_ = 0, max(nums)
    while 10 ** radix < max_:
        buckets = [[] for _ in range(10)]
        for num in nums:
            ind = int((num / 10 ** radix) % 10)
            buckets[ind].append(num)
        
        nums = [num for buck in buckets for num in buck]
        radix += 1
    return nums


if __name__ == '__main__':
    import random
    
    nums = list(range(13))
    random.shuffle(nums)
    print(nums)
    print("桶排序：", bucket_sort(nums))
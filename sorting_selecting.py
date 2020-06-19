__author__ = 'yangbin1729'

# 归并排序
## 基于数组类的归并排序
def merge(s1, s2, s):
    i = j= 0
    while i+j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n//2
    s1 = s[:mid]
    s2 = s[mid:n]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, s)


## 使用基本链表的归并排序
def merge(s1, s2, s):
    while not s1.is_empty() and not s2.is_empty():
        if s1.first() < s2.first():
            s.enqueue(s1.dequeue())
        else:
            s.enqueue(s2.dequeue())
    while not s1.is_empty():
        s.enqueue(s1.dequeue())
    while not s2.is_empty():
        s.enqueue(s2.dequeue())

def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    s1 = LinkedQueue()
    s2 = LinkedQueue()
    while len(s1) < n//2:
        s1.enqueue(s.dequeue())
    while not s.is_empty():
        s2.enqueue(s.dequeue())
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, s)


## 非递归的归并排序
import math
def merge(src, result, start, inc):
    "Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."
    end1 = start+inc
    end2 = min(start+2*inc, len(src))
    x, y, z = start, start+inc, start
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1
    if x < end1:
        result[z:end2] = src[x:end1]
    elif y < end2:
        result[z:end2] = src[y:end2]

def merge_sort(s):
    n = len(s)
    logn = math.ceil(math.log(n, 2))
    src, dest = s, [None]*n
    for i in (2**k for k in range(logn)):       # todo:待理解
        for j in range(0, n, 2*i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if s is not src:
        s[0:n] = src[0:n]



# 快速排序
## 基于队列的快速排序
def quick_sort(s):
    n = len(s)
    if n < 2:
        return
    p = s.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not s.is_empty():
        if s.first() < p:
            L.enqueue(s.dequeue())
        elif p < s.first():
            G.enqueue(s.dequeue())
        else:
            E.enqueue(s.dequeue())
    quick_sort(L)
    quick_sort(G)
    while not L.is_empty():
        s.enque(L.dequeue())
    while not E.is_empty():
        s.enque(L.dequeue())
    while not G.is_empty():
        s.enque(G.dequeue())

## 对 Python 列表的就地快速排序
"""
1.内部使用 while 循环时，索引上界应为 len(seq)-1
2.内部使用 for 循环时，索引上界 len(seq)
"""
def inplace_quick_sort(s, a, b):
    if a >= b:
        return
    pivot = s[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and s[left] < pivot:
            left += 1
        while left <= right and s[right] > pivot:
            right -= 1
        if left <= right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
    s[left], s[b] = s[b], s[left]
    inplace_quick_sort(s, a, left-1)
    inplace_quick_sort(s, left+1, b)



## 对 Python 列表的就地快速排序
def partition(seq, left, right):
    p = seq[left]
    i = left + 1
    for j in range(left+1, right):
        if seq[j] < p:
            seq[j], seq[i] = seq[i], seq[j]
            i += 1
    seq[left], seq[i-1] = seq[i-1], seq[left]
    return i-1

def quickSort(seq,l,r):
    if l >= r:
        return
    j = partition(seq, l, r)
    quickSort(seq, l, j)
    quickSort(seq, j+1, r)
    return seq


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    inplace_quick_sort(a1, 0, len(a1)-1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    inplace_quick_sort(a2,0, len(a2)-1)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    inplace_quick_sort(a3, 0, len(a3)-1)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    inplace_quick_sort(a4, 0, len(a4)-1)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]
    print('Tests pass')

test_quick_sort()
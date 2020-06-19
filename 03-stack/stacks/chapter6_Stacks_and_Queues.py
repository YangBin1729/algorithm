__author__ = 'yangbin1729'

# 栈 todo:flask中对栈数据结构的运用
## 利用 List 实现栈
## todo:初始化时，通过列表生产栈
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def __repr__(self):
        return 'stack(%s)' % str(self._data)


class Empty(Exception):
    pass

## 实现文件中各行逆置
def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


## 分隔符的匹配算法
def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) !=lefty.index(S.pop()):
                return False
    return S.is_empty()

## expr = '[a+{(b+c)+[g]}]'
## is_matched(expr)

## HTML标签是否匹配
def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

# raw = '<div class="col s12 m9"> \
#         <h1 class="header center-on-small-only">关于我们</h1> \
#         <h4 class="light red-text text-lighten-4 center-on-small-only">了解我们的翻译团队.</h4> \
#       </div> '
#
#
# is_matched_html(raw)

# 队列：利用循环数组实现
## todo:初始化时，通过列表生产队列
class ArrayQueue:
    DEFAULT_CAPACITY = 3

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty!')
        return self._data[self._front]

    def dequeue(self):
        """
        根据索引，通过底层列表获取首位元素的值；底层列表该位的值赋值为 None；改变索引值及长度属性值
        % len(self._data)操作是为了让，底层列表值都为 None 时，首位索引重置为 0
        """
        if self.is_empty():
            raise Empty('Queue is empty!')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 <self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front+self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

    def tolist(self):
        return [self._data[(self._front + i) % len(self._data)] for i in range(self._size)]

    def __repr__(self):
        return 'queue(%s)' % str(self.tolist())


# 双端队列
## todo:初始化时，通过列表生产双端队列
class ArrayDeque(ArrayQueue):
    def __init__(self):
        super().__init__()

    def first(self):
        return super().first()

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        _last = (self._front + self._size - 1) % len(self._data)
        return self._data[_last]

    def add_last(self, e):
        super().enqueue(e)

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def delete_first(self):
        return super().dequeue()

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        _last = (self._front + self._size - 1) % len(self._data)
        answer = self._data[_last]
        self._data[_last] = None
        self._size -= 1
        if 0 <self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer

    def tolist(self):
        return [self._data[(self._front + i) % len(self._data)] for i in range(self._size)]

    def __repr__(self):
        return 'deque(%s)' % str(self.tolist())

# Python collections 模块中的双端队列
from collections import deque
"""
deque 基于双向链表，.append()和.pop()方法都是原子化操作，所以是线程安全的。但部分其他方法不是原子化操作，也不是线程安全

"""
from queue import LifoQueue
"""
LifoQueue 线程安全
"""



# todo:练习
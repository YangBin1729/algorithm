__author__ = 'yangbin1729'

# Hashing
"""
将任意尺寸数据转化为固定尺寸数据的概念，将字符串转化为整数
"""
def test_ord_hash():
    print('hello world:', sum(map(ord, 'hello world')))
    print('dello worlh:', sum(map(ord, 'dello worlh')))

# test_ord_hash()


# Perfect hashing functions
"""
避免上述不同字符串，但仅仅字符顺序不同，所以哈希值相同的情况
"""

def myhash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult*ord(ch)
        mult += 1
    return hv

def test_myhash():
    for item in ('hello world', 'world hello', 'gello xorld'):
        print("{}:{}".format(item, myhash(item)))

    for item in ('ad', 'ga'):
        print("{}:{}".format(item, myhash(item)))

# test_myhash()


# Hash table
"""
通过关键字而不是整数值来获取元素 
"""
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return str((self.key, self.value))

class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None]*self.size
        self.count = 0

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)

        "当内部列表 h 处非None时，在 h 后面查找第一个 None，然后将元素添加至此处"
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h+1) % self.size

        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

    def get(self, key):
        h = self._hash(key)

        "当内部列表 h 处项的 key 与被查找的 key 不同时，向后方查找"
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+1) % self.size
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

def test_hashtable():
    ht = HashTable()
    ht.put('good', 'eggs')
    ht.put("better", "ham")
    ht.put("best", "spam")
    ht.put("ad", "do not")
    ht.put("ga", "collide")

    for key in ("good", "better", "best", "worst", "ad", "ga"):
        v = ht[key]
        print(v)

    print("The number of elements is: {}".format(ht.count))

# test_hashtable()

# Non-string keys
"""
关键字不一定要是字符串。可以自定义类作为关键字，需要重载 __hash__()方法
"""

# Growing a hash table
"""
1.哈希表有一个初始 size ，当不断添加元素后，当表要被填满时，就需要将表增大；
2.用 count/size 表示哈希表的 load factor，通常当该参数为 0.75 时，增大表
"""

# Chaining
"""
1.上述发生冲突后，从 slots 当前位置依次向后查找；当表尺寸变大后，查找速度会越来越慢；
2.将内部 slots 列表的元素都设置为 列表 形式
3.添加新元素时，先根据哈希值查找到 slots 中的那个元素列表，然后将新元素添加到该元素列表尾部
4.将内部 slots 列表的元素设置为 二叉搜索树 形式，进一步提高效率
"""

# Symbol tables


## Sets
class HashSet:
    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.numItems = 0
        for item in contents:
            self.add(item)

    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1
        while items[idx] != None:
            if items[idx] == item:
                return False
            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx
            idx += (idx+1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, newList)
        return newList

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None]*2*len(self.items))

    def __remove(item, items):
        idx = hash(item) % len(items)
        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True
            idx = (idx + 1) % len(items)
        return False

    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))
        else:
            raise KeyError('Item not in HashSet')

    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True
            idx = (idx+1) % len(self.items)
        return False

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]

    def difference_update(self, other):
        for item in other:
            self.remove(item)

    def difference(self, other):
        result = HashSet(self)
        result.difference_update(other)
        return result



# ## Solving Sudoku
# def to_int(x):
#     if x.isdigit():
#         return int(x)
#     return x
#
# board = [[to_int(x) for x in row.split(' ')] for row in """
# x x x x x x x x x
# x x x x 1 x x 9 2
# x 8 6 x x x x 4 x
# x x 1 5 6 x x x x
# x x x x x 3 6 2 x
# x x x x x x 5 x 7
# x 3 x x x x x 8 x
# x 9 x 8 x 2 x x x
# x x 7 x x 4 3 x x
# """.split('\n') if row
# ]
#
# print(board)
#
#
# nums = set(range(1, 10))
#
# def get_col(board, j):
#     return set(board[i][j] for i in range(9))
#
#
# def get_box(board, i, j):
#     m, n = i // 3, j // 3
#     return set(board[m * 3][n * 3:n * 3 + 3] +\
#                board[m * 3 + 1][n * 3:n * 3 + 3] +\
#                board[m * 3 + 2][n * 3:n * 3 + 3])
#
#
#
# def plays(board, i, j):
#     if board[i][j] == 'x':
#         row = set(board[i])
#         col = get_col(board, j)
#         box = get_box(board, i, j)
#         return nums - (row|col|box)
#
# def test():
#     assert plays(board, 0, 7) == set([1,3,5,6,7])
#     assert plays(board, 2, 1) == None
#     assert plays(board, 8, 1) == set([1,2,5,6])
#     print('tests pass')
#
# test()


from collections import MutableMapping

# 映射基类
class MapBase(MutableMapping):

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


# 利用 python 列表作为未排序表实现的 map
class UnsortedTableMap(MapBase):

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error:' + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j].key:
                self._table.pop(j)
                return
        raise KeyError('Key Error:' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key


# 基于映射基类实现的哈希表基类
from random import randrange

class HashMapBase(MapBase):

    def __init__(self, cap=11, p=109345121):
        self._table = [None] * cap
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table)//2:
             self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

# 用分离链表实现的具体哈希映射类
class ChainHashMap(HashMapBase):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

# 用线性探测处理冲突的 ProbeHashMap 类的具体实现
class ProbeHashMap(HashMapBase):
    _AVAIL = object()

    def _is_avaliable(self, j):
        return self._table[j] is not None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        firstAVAIL = None
        while True:
            if self._is_avaliable(j):
                if firstAVAIL is None:
                    firstAVAIL = j
                if self._table[j] is None:
                    return (False, firstAVAIL)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j+1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error:' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error:' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_avaliable(j):
                yield self._table[j]._key

# 排序检索表
class SortedTableMap(MapBase):

    def _find_index(self, k, low, high):
        if high < low:
            return high+1
        else:
            mid = (low + high)//2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid-1)
            else:
                return  self._find_index(k, mid+1, high)

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) -1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error:' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self._table) -1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) and self._table[j]._key != k:
            raise KeyError('Key Error:' + repr(k))
        self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if len(self._table) > j:
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)

        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1

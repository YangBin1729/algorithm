__author__ = 'yangbin1729'

# 树的抽象基类
class Tree:

    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        def __eq(self):
            raise NotImplementedError('must be implemented by subclass')
        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def positions(self):
        return self.preorder()

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()


# 二叉树抽象基类
class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


## 二叉树的链式储存结构
class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p dose not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None: raise ValueError('Root exists')
        self._szie = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError('Left child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._elemnt = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


## todo:二叉树的数组表示
## todo：一般树的链式储存结构

# todo：树的遍历算法

## 1.树的先序遍历
"""
def preorder(self):
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()):
            yield p
            
def _subtree_preorder(self, p):
    yield p 
    for c in self.children(p):
        for other in self._subtree_preorder(c):
            yield other
            
def positions(self):
    return self.preorder()    
"""

## 2.树的后序遍历
"""
def postorder(self):
    if not self.is_empty():
        for p in self._subtree_postorder(self.root()):
            yield p

def _subtree_postorder(self, p):
    for c in self.children(p):
        for other in self._subtree_postorder(c):
            yield other
    yield p
"""
## 3.树的广度优先遍历
"""
def breadfirst(self):
    if not self.is_empty():
        fringe = LinkedQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            for c in self.children(p):
                fringe.enqueue(c)
"""
## 4.二叉树的中序遍历
"""
def inorder(self):
    if not self.is_empty():
        for p in self._subtree_inorder(self.root()):
            yield p

def _subtree_inorder(self, p):
    if self.left(p) is not None:
        for other in self._subtree_inorder(self.left(p)):
            yield other
    yield p
    if self.right(p) is not None:
        for other in self._subtree_inorder(self.right(p)):
            yield other

def position(self):
    return self.inorder()   
"""

# todo:树遍历的应用
## 1.目录表
def preorder_indent(T, p, d):
    print(2*d*' ' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d+1)

def preorder_label(T, p, d, path):
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.elemet())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()
## 2.




# todo：如何根据已有数据生成树？？？？


























### an abstract syntax tree of (5+4)*6+3: An infix expression,操作符在数字中间
class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

def compute():
    x = NumNode(5)
    y = NumNode(4)
    p = PlusNode(x, y)
    t = TimesNode(p, NumNode(6))
    root = PlusNode(t, NumNode(3))
    print(root.eval())

compute()

### an abstract syntax tree of (5+4)*6+3: An postfix expression，操作符在数字后行，5 4 + 6 * 3 +
class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " * " +self.right.inorder() + ")"


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " + " +self.right.inorder() + ")"


class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        return str(self.num)

### (5+4)*6+3: An prefix expression，操作符在数字前面，+ * + 5 4 6 3

### An prefix expression Parser todo:可以和 dcp 课程结合起来！！！
import queue

def E(q):
    if q.empty():
        raise ValueError("Invalid Prefix Expression")

    token = q.get()

    if token == "+":
        return PlusNode(E(q), E(q))     # left 和 right 都为 E(q)!!!

    if token == "*":
        return TimesNode(E(q), E(q))

    return NumNode(float(token))

def test_E():
    x = "+ * + 5 4 6 3"
    lst = x.split()
    q = queue.Queue()

    for token in lst:
        q.put(token)

    root = E(q)

    print(root.eval())
    print(root.inorder())

# test_E()


### The BinarySearchTree Class
class BinarySearchTree:
    class _Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        def getVal(self):
            return self.val
        def setVal(self, newVal):
            self.val = newVal
        def getLeft(self):
            return self.left
        def getRight(self):
            return self.right
        def setLeft(self, newleft):
            self.left = newleft
        def setRight(self, newright):
            self.right = newright
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
            yield self.val
            if self.right != None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(root, val):             # todo:需要好好理解！！！
            if root == None:
                return BinarySearchTree._Node(val)
            if val < root.getVal():
                root.setLeft(_insert(root.getLeft(), val))
            else:
                root.setRight(_insert(root.getRight(), val))
            return root
        self.root = _insert(self.root, val)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

def test_binary_search_tree():
    s = "6 2 4 3 5 1 9 10"
    lst = s.split()

    tree = BinarySearchTree()
    for x in lst:
        tree.insert(float(x))
    for x in tree:
        print(x)

test_binary_search_tree()

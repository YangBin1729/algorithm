__author__ = 'yangbin1729'

from .abstractCollection import AbstractCollection
from .bstnode import BSTNode

class LinkedBST(AbstractCollection):
    def __init__(self, sourceCollection=None):
        self._root = None
        AbstractCollection.__init__(sourceCollection)

    def find(self, item):
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self._root)

    def inorder(self):
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def __str__(self):
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level+1)
                s +=" ".level
                s += str(node.data) + '\n'
                s += recurse(node.left, level+1)
            return s
        return recurse(self._root, 0)

    def add(self, item):
        def recurse(node):
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)

        if self.isEmpty():
            self._root = BSTNode(item)
        else:
            recurse(self._root)

        self._size += 1


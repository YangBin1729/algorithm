__author__ = 'yangbin1729'


class Tree:

    # ------------------------------- nested Position class -------------------------------
    class Position:

        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
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

    def _height1(self):  # works, but O(n^2) worst-case time
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):  # time is linear in size of subtree
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)  # start _height2 recursion

    def __iter__(self):
        for p in self.positions():  # use same order as positions()
            yield p.element()  # but yield each element

    def positions(self):
        return self.preorder()  # return entire preorder iteration

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # start recursion
                yield p

    def _subtree_preorder(self, p):
        yield p  # visit p before its subtrees
        for c in self.children(p):  # for each child c
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other  # yielding each to our caller

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):  # for each child c
            for other in self._subtree_postorder(c):  # do postorder of c's subtree
                yield other  # yielding each to our caller
        yield p  # visit p after its subtrees

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()  # known positions not yet yielded
            fringe.enqueue(self.root())  # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()  # remove from front of the queue
                yield p  # report this position
                for c in self.children(p):
                    fringe.enqueue(c)  # add children to back of queue

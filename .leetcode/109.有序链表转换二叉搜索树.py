#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (69.37%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    24.8K
# Total Submissions: 34.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
#
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = f'{self.val}'
        tmp = self.next
        while tmp is not None:
            s += f'-->{tmp.val}'
            tmp = tmp.next
        return s + '-->NULL'

    def __repr__(self):
        return self.__str__()


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        def _helper(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(vals[mid])

            if l == r:
                return node

            node.left = _helper(l, mid - 1)
            node.right = _helper(mid + 1, r)
            return node

        return _helper(0, len(vals) - 1)


# @lc code=end

vals = [-10, -3, 0, 5, 9]
nodes = [ListNode(val) for val in vals]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]

print(Solution().sortedListToBST(head))
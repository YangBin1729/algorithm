#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (62.73%)
# Likes:    180
# Dislikes: 0
# Total Accepted:    55.1K
# Total Submissions: 87.7K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [1,2,3]
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#
from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def preorderTraversal_1(self, root: TreeNode) -> List[int]:
        """
        1. 递归
        """
        res = []
        if root:
            res.append(root.val)
            res.extend(self.preorderTraversal_1(root.left))
            res.extend(self.preorderTraversal_1(root.right))
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        2.基于栈
        """
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res


# @lc code=end

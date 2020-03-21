#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (57.84%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    30.7K
# Total Submissions: 52.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
# 返回:
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
#
#
#

from typing import List


# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum_1(self, root: TreeNode, target: int) -> List[List[int]]:
        """
        1. 栈，保存节点路径和剩余的值
        """
        res = []
        if not root:
            return res

        stack = [([root], target - root.val)]
        while stack:
            path, target = stack.pop()
            root = path[-1]

            if not root.left and not root.right and target == 0:
                res.append([node.val for node in path])

            if root.left:
                stack.append((path + [root.left], target - root.left.val))
            if root.right:
                stack.append((path + [root.right], target - root.right.val))
        return res

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        """
        2. 栈，保存节点和值列表
        """
        res = []
        if not root:
            return res

        stack = [(root, [root.val])]
        while stack:
            root, vals = stack.pop()
            if not root.left and not root.right and sum(vals)==target:
                res.append(vals)
            if root.left:
                stack.append((root.left, vals+[root.left.val]))
            if root.right:
                stack.append((root.right, vals+[root.right.val]))
        return res


# @lc code=end

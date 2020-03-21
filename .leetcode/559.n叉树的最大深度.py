#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (67.37%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 24.3K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 我们应返回其最大深度，3。
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    def maxDepth(self, root: 'Node') -> int:
        """
        1. 递归
        """
        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            return 1 + max([self.maxDepth(child) for child in root.children])

        # TODO:栈的解法


# @lc code=end

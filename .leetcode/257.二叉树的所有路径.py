#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (61.01%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 40.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 输入:
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """
        DFS，栈
        """
        res = []
        if not root:
            return res

        stack = [(f"{root.val}", root)]
        while stack:
            path, root = stack.pop()
            if not root.left and not root.right:
                res.append(path)
            if root.left:
                stack.append((path + f"->{root.left.val}", root.left))
            if root.right:
                stack.append((path + f"->{root.right.val}", root.right))
        return res


# @lc code=end

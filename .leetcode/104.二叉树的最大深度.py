#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (71.43%)
# Likes:    404
# Dislikes: 0
# Total Accepted:    103.2K
# Total Submissions: 144.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最大深度 3 。
#
#


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

    def maxDepth_1(self, root: TreeNode) -> int:
        """
        1. 递归
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root: TreeNode) -> int:
        # 2. 栈+迭代
        # KEY：栈代替递归
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack:
            curr_depth, root = stack.pop()
            if root is not None:
                depth = max(curr_depth, depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))
        return depth


# @lc code=end

#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (40.62%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    41.3K
# Total Submissions: 101.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最小深度  2.
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

    def minDepth_1(self, root: TreeNode) -> int:
        """
        1. 递归
        """
        if not root:
            return 0
        elif (not root.left) and (not root.right):
            return 1
        return 1 + min(
            self.minDepth(root.left) if root.left else float('inf'),
            self.minDepth(root.right) if root.right else float('inf'))

    def minDepth(self, root: TreeNode) -> int:
        # 2. 栈 + 深度优先搜索
        # KEY: 关键点——栈替代递归！
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root)], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))
        return min_depth

        # TODO：广度优先搜索


# @lc code=end

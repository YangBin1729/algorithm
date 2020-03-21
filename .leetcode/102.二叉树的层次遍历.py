#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (59.90%)
# Likes:    334
# Dislikes: 0
# Total Accepted:    65.5K
# Total Submissions: 109.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其层次遍历结果：
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
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

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        1. BFS
        curr 表示一层的所有节点。代码简洁，但 curr 每次都进行了两次遍历       
        """

        res, curr = [], [root]
        while any(curr):
            res.append([node.val for node in curr])
            curr = [child for node in curr for child in [node.left, node.right] if child]

        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        2. BFS 
        next_level 表示下一层节点，一次遍历；
        level_val 表示当前层的值；
        """
        res, curr = [], [root]
        while any(curr):
            level_val = []
            next_level = []
            for node in curr:
                level_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(level_val)
            curr = next_level
        return res

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        """
        3. DFS + 递归
        并不是按层访问，只是将每层的值组合在同一个列表中
        """
        res = []

        def helper(node, level):     # 通过 level 记录当前所在的层次；并不是一次性将一层访问完
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)

            helper(node.left, level + 1)     # 递归调用时，会先将所有的左节点访问完
            helper(node.right, level + 1)     # 再访问右节点，所以是深度优先搜索

        helper(root, 0)

        return res


# @lc code=end

#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.97%)
# Likes:    347
# Dislikes: 0
# Total Accepted:    54.9K
# Total Submissions: 195.7K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
#
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
    def isValidBST_1(self, root: TreeNode) -> bool:
        """
        1. 中序遍历创建值的列表，判断值列表是否递增
        直接递归比较左、根、右，结果不正确，右子树所有点的值要大于根......
        """
        val_list = []

        def inorderTransverse(root):
            if root:
                inorderTransverse(root.left)
                val_list.append(root.val)
                inorderTransverse(root.right)
            return

        inorderTransverse(root)

        for i in range(len(val_list) - 1):
            if val_list[i + 1] <= val_list[i]:
                return False
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        """
        2.迭代 
        KEY: 上下限制，右子树最小值大于根，左子树最大值小于根
        """
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val<=lower or val>=upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


# @lc code=end

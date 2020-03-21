#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (66.28%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    27.4K
# Total Submissions: 40.6K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为链表。
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        1. 先序遍历
        """
        if not root:
            return root 
            
        curr = root
        stack = [child for child in [root.right, root.left] if child]
        while stack:
            next = stack.pop()
            if next.right:
                stack.append(next.right)
            if next.left:
                stack.append(next.left)
            
            curr.left = None
            curr.right = next

            curr = next
               








# @lc code=end


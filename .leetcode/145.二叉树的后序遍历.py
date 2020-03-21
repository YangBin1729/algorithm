#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (68.96%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    41.8K
# Total Submissions: 60.5K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 1.递归
        # res = []
        # if root:
        #     res.extend(self.postorderTraversal(root.left))
        #     res.extend(self.postorderTraversal(root.right))
        #     res.append(root.val)
        # return res

        # 2.栈
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        return res[::-1]




# @lc code=end


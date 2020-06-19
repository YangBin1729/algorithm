#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (56.66%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 9.7K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
#
# 示例：
#
#
# 输入:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# 输出: [1, 3, 9]
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

    def largestValues2(self, root: TreeNode) -> List[int]:
        """
        每层的节点循环两次
        """
        res, curr = [], [root]
        while any(curr):
            res.append(max([node.val for node in curr if node]))
            curr = [child for node in curr for child in [node.left, node.right] if child]
        return res


    def largestValues3(self, root: TreeNode) -> List[int]:
        res, level = [], [root]
        while any(level):
            lvl_max = float('-inf')
            next_lvl = []
            for node in level:
                lvl_max = max(lvl_max, node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)

            res.append(lvl_max)
            level = next_lvl
        return res


    def largestValues(self, root: TreeNode) -> List[int]:
        """
        记录节点所在的层
        """
        res = []
        if not root:
            return res 
            
        stack = [(root, 0)]
        while stack:
            node, ind = stack.pop()
            if ind == len(res):
                res.append(node.val)
            else:
                res[ind] = max(res[ind], node.val)

            if node.right:
                stack.append((node.right, ind+1))
            if node.left:
                stack.append((node.left, ind + 1))
        return res 



# @lc code=end

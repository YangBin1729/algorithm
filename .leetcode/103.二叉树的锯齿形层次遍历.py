#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (52.77%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 62.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回锯齿形层次遍历如下：
#
# [
# ⁠ [3],
# ⁠ [20,9],
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

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root:
            return []

        queue = deque([root])
        i = 0
        res = []
        while queue:
            nxt_queue = deque()
            curr = []
            while queue:
                node = queue.popleft()
                curr.append(node.val)
                if i % 2 == 0:
                    for child in [node.left, node.right]:     # 偶数层
                        if child:
                            nxt_queue.appendleft(child)
                else:
                    for child in [node.right, node.left]:     # 偶数层
                        if child:
                            nxt_queue.appendleft(child)
            queue = nxt_queue
            res.append(curr)
            i += 1
        return res


# @lc code=end

vals = list(range(9))
nodes = [TreeNode(val) for val in vals]
for i in range(4):
    nodes[i].left = nodes[2 * i + 1]
    nodes[i].right = nodes[2 * i + 2]
root = nodes[0]

print(Solution().zigzagLevelOrder(root))

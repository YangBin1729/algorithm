#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (49.15%)
# Likes:    615
# Dislikes: 0
# Total Accepted:    95.4K
# Total Submissions: 190.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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

    def isSymmetric_1(self, root: TreeNode) -> bool:
        """
        层序遍历，每层的值列表应该对称
        """

        from collections import deque
        if not root:
            return True

        level = [root.left, root.right]
        while any(level):
            # level_val = []
            # next_level = []
            # for node in level:
            #     if node:
            #         level_val.append(node.val)
            #         next_level.extend([node.left, node.right])
            #     else:
            #         level_val.append(None)

            # if len(level) % 2 or level_val != level_val[::-1]:     # 列表逆置操作是优化点：双指针
            #     return False
            # level = next_level

            next_level = deque()
            i, j = 0, len(level) - 1
            while i < j:
                if level[i] and level[j]:
                    if level[i].val != level[j].val:
                        return False
                    else:
                        next_level.appendleft(level[i].right)
                        next_level.appendleft(level[i].left)
                        next_level.append(level[j].left)
                        next_level.append(level[j].right)
                        i += 1
                        j -= 1
                elif level[i]==level[j]==None:
                    i += 1
                    j -= 1
                else:
                    return False
            level = next_level
        return True


    def isSymmetric(self, root: TreeNode) -> bool:
        """
        问题转换成两棵树是否为镜像
        """
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val==t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)



# @lc code=end

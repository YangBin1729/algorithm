#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (58.45%)
# Likes:    311
# Dislikes: 0
# Total Accepted:    35.2K
# Total Submissions: 60.1K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#
#
# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
#
# 示例 2:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#
#
#
# 说明:
#
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
#
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        # 1.递归：时间及空间复杂度皆为 O(N)
        # KEY: 解法
        # 前提：p\q 一定为该树的节点；否则当只能找到 p\q 中的一个时，结果为该节点
        # p\q 的 LCA 在 root.left 分支里，则 right = None, left 为结果
        # p\q 的 LCA 在 root.right 分支里，则 left = None, right 为结果
        # left\right 都不为 None，则 p\q 在 left\right 一边一个，root为结果
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        # 2.查找节点并保存路径，路径交叉点为结果
        # KEY:关键点：以词典的形式保存路径！！！
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

    def lowestCommonAncestor_3(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        # TODO: 3.待理解！！！
        # 三个常量分别表示：子节点待访问、子节点已访问
        BOTH_PENDING = 2
        BOTH_DONE = 0

        stack = [(root, BOTH_PENDING)]
        one_node_found = False

        LCA_index = -1

        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != BOTH_DONE:
                if parent_state == BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1

                    child_node = parent_node.left
                else:
                    child_node = parent_node.right

                stack.pop()
                stack.append((parent_node, parent_state - 1))

                if child_node:
                    stack.append((child_node, BOTH_PENDING))
            else:

                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None


# @lc code=end

if __name__ == "__main__":

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    nodes = [TreeNode(i) for i in range(1, 8)]
    for i in range(3):
        nodes[i].left = nodes[2 * i + 1]
        nodes[i].right = nodes[2 * i + 2]

    root = nodes[0]
    p = nodes[3]
    q = TreeNode(9)
    r = Solution().lowestCommonAncestor(root, p, q)
    print(r.val)

#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (60.33%)
# Likes:    338
# Dislikes: 0
# Total Accepted:    25.7K
# Total Submissions: 41.3K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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

    def generateTrees(self, n: int) -> List[TreeNode]:

        res = []

        def _generate(cur, nums, i):
            if cur > n:
                vals = [num for num in nums if num != 0]
                res.append(vals)
                return

            # 下一个值的放置位置
            if 0 < 2 * i + 1 < 2**n and nums[2 * i + 1] == 0:
                nums[2 * i + 1] = cur
                _generate(cur + 1, nums, 2 * i + 1)
                nums[2 * i + 1] = 0 # 还原状态

            if i % 2 == 0 and 0 < i // 2 < 2**n and nums[i // 2] == 0:
                nums[i // 2] = cur
                _generate(cur + 1, nums, i // 2)
                nums[i // 2] = 0 # 还原状态

        for i in range(1, 2**n):
            nums = [0] * (2**n)
            nums[i] = 1
            _generate(2, nums, i)

        return res


# @lc code=end

print(Solution().generateTrees(3))
#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (69.19%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 22.2K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#

from typing import List


# @lc code=start
class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # TODO
        ans = []

        def helper(k, start, n, tmp):
            if k == 0:
                if n == 0:
                    ans.append(tmp)
                return
            for i in range(start, 10):
                if n - i < 0:
                    break
                helper(k - 1, i + 1, n - i, tmp + [i])

        helper(k, 1, n, [])
        return ans


# @lc code=end

print(Solution().combinationSum3(3, 9))
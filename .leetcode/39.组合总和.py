#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (67.44%)
# Likes:    553
# Dislikes: 0
# Total Accepted:    72K
# Total Submissions: 104.9K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#

from typing import List


# @lc code=start
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def _helper(curr, candidates, sum):
            if sum == target:
                res.append(curr)
                return
            if sum < target and candidates:
                for i in range(len(candidates)):
                    _helper(curr + [candidates[i]], candidates[i:], sum + candidates[i])

        _helper([], candidates, 0)
        return res


# @lc code=end

candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
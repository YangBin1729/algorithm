#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (58.63%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    44.4K
# Total Submissions: 73.2K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
#
#

from typing import List


# @lc code=start
class Solution:

    def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()

        def _helper(curr, candidates, sum):
            if sum == target and tuple(sorted(curr)) not in visited:     # 哈希表去重
                res.append(curr)
                visited.add(tuple(sorted(curr)))
                return
            if sum < target and candidates:
                for i in range(len(candidates)):
                    _helper(curr + [candidates[i]], candidates[i + 1:], sum + candidates[i])

        _helper([], candidates, 0)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def _helper(i, curr, rem):
            if rem == 0:
                res.append(curr[:])
                return
            for j in range(i, len(candidates)):
                if candidates[j] > rem:
                    break
                if j > i and candidates[j - 1] == candidates[j]:     # 排序后便于去重
                    continue

                curr.append(candidates[j])
                _helper(j + 1, curr, rem - candidates[j])
                curr.pop()

        candidates.sort()
        _helper(0, [], target)

        return res


# @lc code=end

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
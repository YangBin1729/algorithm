#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (57.83%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    25.1K
# Total Submissions: 42.4K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#

from typing import List


# @lc code=start
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()     # KEY：先排序，后续才能方便进行去重
        for num in nums:
            ans.extend([item + [num] for item in ans if item + [num] not in ans])
        return ans


# @lc code=end

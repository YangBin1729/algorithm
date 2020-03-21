#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (75.56%)
# Likes:    415
# Dislikes: 0
# Total Accepted:    50.4K
# Total Submissions: 66.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

from typing import List


# @lc code=start
class Solution:

    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        """
        KEY：简洁巧妙的解法
        """
        res = [[]]
        for num in nums:
            res = res + [[num] + subset for subset in res]
        return res

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        """
        2. 库函数
        """
        from itertools import combinations
        res = []
        for i in range(len(nums) + 1):
            for comb in combinations(nums, i):
                res.append(comb)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        3. 回溯算法
        TODO：
        """
        res = []
        n = len(nums)

        def backtrack(i, subset):
            res.append(subset)
            for j in range(i, n):
                backtrack(j + 1, subset + [nums[j]])
        
        backtrack(0, [])
        return res


# @lc code=end

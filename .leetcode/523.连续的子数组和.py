#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
# https://leetcode-cn.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (22.40%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 29.3K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n
# 也是一个整数。
#
# 示例 1:
#
# 输入: [23,2,4,6,7], k = 6
# 输出: True
# 解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
#
#
# 示例 2:
#
# 输入: [23,2,6,4,7], k = 6
# 输出: True
# 解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
#
#
# 说明:
#
#
# 数组的长度不会超过10,000。
# 你可以认为所有数字总和在 32 位有符号整数范围内。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def checkSubarraySum_1(self, nums: List[int], k: int) -> bool:
        """
        1. 暴力遍历
        """

        for i in range(len(nums) - 1):
            subarray_sum = nums[i]
            for j in range(i + 1, len(nums)):
                subarray_sum += nums[j]
                if k == 0:
                    if subarray_sum == 0:
                        return True
                elif subarray_sum % k == 0:
                    return True
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        2. 哈希表
        """
        sum = 0
        lookup = {sum: -1}
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                sum = sum % k
            if sum in lookup:
                if i - lookup.get(sum) > 1:
                    return True
            else:
                lookup[sum] = i
        return False


# @lc code=end

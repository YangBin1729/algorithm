#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (36.70%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 93.2K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j
# 的差的绝对值最大为 k。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
#
#
from typing import List


# @lc code=start
class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = set()
        for i, num in enumerate(nums):
            if i > k:
                d.remove(nums[i - k - 1])
            if num in d:
                return True
            else:
                d.add(num)
        return False


# @lc code=end

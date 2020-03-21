#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.35%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    17K
# Total Submissions: 47.5K
# Testcase Example:  '[2,3,2]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
#
# 示例 2:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
#
from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        KEY: 转化成两个数组，一个不包含尾元素、一个不包含首元素
        """
        def _rob(nums):
            currMax, prevMax = 0, 0
            for num in nums:
                prevMax, currMax = currMax, max(currMax, prevMax + num)
            return currMax
        return max(_rob(nums[:-1]), _rob(nums[1:]))  if len(nums) != 1 else nums[0]


# @lc code=end

#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (32.49%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 16.8K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
# 示例 1:
#
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
#
#
# 示例 2:
#
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#
#
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
#
#

from typing import List


# @lc code=start
class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        # TODO
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        i = len(nums) - 1

        return dp
        
                


# @lc code=end

nums = [1,3,5,4,7]
print(Solution().findNumberOfLIS(nums))


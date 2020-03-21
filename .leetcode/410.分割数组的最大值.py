#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
# https://leetcode-cn.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (39.87%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 11.1K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
#
# 注意:
# 数组长度 n 满足以下条件:
#
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
#
#
# 示例:
#
#
# 输入:
# nums = [7,2,5,10,8]
# m = 2
#
# 输出:
# 18
#
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def splitArray(self, nums: List[int], m: int) -> int:
        """
        # TODO：超时
        动态规划：
        - dp[i][j] --> 前 j 个数字 nums[:j] 分割成 i 个子数组时的结果
            - 将前 k 个数字分成 i-1 组，第 k~j 个数字为 1 组
            - 遍历 
            - 找出最小

        """

        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(1, n + 1):
            dp[1][j] = sum(nums[:j]) # 前 j 个数字分成 1 个子组

        for i in range(2, m + 1):
            for j in range(i, n + 1):
                dp[i][j] = float("inf")

                tmp = 0
                for k in range(j - 1, i - 2, -1):
                    tmp += nums[k]
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], tmp))

                # for k in range(i - 1, j):
                #     sub_nums = nums[k:j]
                #     dp[i][j] = min(dp[i][j], max(dp[i - 1][k], sum(sub_nums)))
                # 将前 k 个数字分成 i-1 组，第 k~j 个数字为 1 组
                
        return dp[m][-1]


# @lc code=end

nums = [7, 2, 5, 10, 8]
m = 4
print(Solution().splitArray(nums, m))

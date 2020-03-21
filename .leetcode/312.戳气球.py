#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (56.38%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 13.8K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
# left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
#
# 求所能获得硬币的最大数量。
#
# 说明:
#
#
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# 示例:
#
# 输入: [3,1,5,8]
# 输出: 167
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#
#

from typing import List


# @lc code=start
class Solution:

    def maxCoins_1(self, nums: List[int]) -> int:
        """
        贪心算法：每一步选择左右乘积最大的气球
        错误！
        """

        def getMax(nums):
            if len(nums) == 1:
                return 0, nums[0]

            l_mul_r, max_ind = 0, 0
            res = 0
            for i in range(len(nums)):
                if i == 0:
                    tmp = nums[1]
                elif i == len(nums) - 1:
                    tmp = nums[i - 1]
                else:
                    tmp = nums[i - 1] * nums[i + 1]

                if tmp > l_mul_r:
                    l_mul_r = tmp
                    res = l_mul_r * nums[i]
                    max_ind = i
            return max_ind, res

        ans = 0
        while nums:
            max_ind, res = getMax(nums)
            ans += res
            nums.pop(max_ind)
        return ans

    def maxCoins(self, nums: List[int]) -> int:
        """
        # TODO:
        动态规划：
        - 从最后一步出发，最后一步必定扎破一个气球编号为 i，获得金币 1*nums[i]*1；
        - 此时 1~i-1 及 i+1~n 个气球都已被扎破，需要求两侧的最大值；

        - dp[i][j] 表示扎破 i+1~j-1 号气球能获得的金币数
            - 遍历 i+1~j-1 气球，选择第 k 个为最后一个扎破的气球
            - dp[i][j] = dp[i][k] + a[i]*a[k]*a[j] + dp[k][j]

        """

        nums = [1] + nums + [1]

        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]


# @lc code=end

nums = [3, 1, 5, 8]
print(Solution().maxCoins(nums))

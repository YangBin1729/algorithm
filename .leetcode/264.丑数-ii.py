#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (48.17%)
# Likes:    210
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 32.9K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
# 说明:
#
#
# 1 是丑数。
# n 不超过1690。
#
#
#


# @lc code=start
class Solution:

    def nthUglyNumber_1(self, n: int) -> int:
        """
        FIXME：超时
        求 n=15
        n=14 时为 20
        20//2 = 10 --> 11 不是丑数 --> 12 是 --> 12*2=24
        20//3 = 6 --> 7 不是丑数 --> 8 是 --> 8*3=24
        20//5= 4 --> 5 是丑数 --> 5*5=25
        """
        dp = [1] * n
        s = set([1])
        for i in range(1, n):
            dp[i] = float('inf')
            for factor in [2, 3, 5]:
                r = dp[i - 1] // factor
                for k in range(r + 1, dp[i - 1] + 1):
                    if k in s:
                        dp[i] = min(dp[i], k * factor)
                        break
            s.add(dp[i])
        return dp[-1]

    def nthUglyNumber(self, n: int) -> int:
        """
        动态规划
        """
        dp = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1, n):
            min_val = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            dp[i] = min_val
            if dp[i2] * 2 == min_val:
                i2 += 1
            if dp[i3] * 3 == min_val:
                i3 += 1
            if dp[i5] * 5 == min_val:
                i5 += 1
        return dp[-1]


# @lc code=end

print(Solution().nthUglyNumber(276))
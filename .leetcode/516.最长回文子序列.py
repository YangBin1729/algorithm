#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (47.68%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 26.1K
# Testcase Example:  '"bbbab"'
#
# 给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。
#
# 示例 1:
# 输入:
#
#
# "bbbab"
#
#
# 输出:
#
#
# 4
#
#
# 一个可能的最长回文子序列为 "bbbb"。
#
# 示例 2:
# 输入:
#
#
# "cbbd"
#
#
# 输出:
#
#
# 2
#
#
# 一个可能的最长回文子序列为 "bb"。
#
#


# @lc code=start
class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        动态规划
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[j][j] = 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


# @lc code=end

s = "bbbab"
print(Solution().longestPalindromeSubseq(s))
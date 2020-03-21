#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Hard (37.68%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 26.6K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
#
# 示例 1:
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
#
#
# 示例 2:
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false
#
#


# @lc code=start
class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符，与 s3 的前 i+j 个字符是否是交错字符串
        """
        n, m = len(s1), len(s2)
        l = len(s3)
        if m + n != l:
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(1, m + 1):
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True

        for i in range(1, n + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (s3[i + j - 1] == s1[i - 1] and
                            dp[i - 1][j]) or (s3[i + j - 1] == s2[j - 1] and dp[i][j - 1])
        return dp[-1][-1]


# @lc code=end

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().isInterleave(s1, s2, s3))
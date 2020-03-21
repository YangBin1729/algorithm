#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (40.61%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 19K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回符合要求的最少分割次数。
#
# 示例:
#
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#
#
#


# @lc code=start
class Solution:

    def minCut(self, s: str) -> int:
        """
        动态规划
        - dp[i][j] 表示 s[i:j+1] 是否是回文串
        - res[i] 表示 s[i:] 的最少分割次数
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1

        res = list(range(n - 1, -1, -1))
        for i in range(n - 2, -1, -1):
            if dp[i][-1] == 1:
                res[i] = 0
                continue
            for j in range(i, n):
                if dp[i][j]:
                    res[i] = min(res[i], 1 + res[j + 1])
        print(res)
        return res[0]


# @lc code=end

s = 'aab'
print(Solution().minCut(s))
#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (59.56%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 24.4K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
# 示例 1:
#
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#
#
# 示例 2:
#
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#
#
# 注意:
#
#
# 输入的字符串长度不会超过1000。
#
#
#


# @lc code=start
class Solution:

    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        dp = [[0] * len(s) for _ in range(len(s))]

        for j in range(len(s)):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    res += 1
        return res


# @lc code=end

s = 'abc'
Solution().countSubstrings(s)


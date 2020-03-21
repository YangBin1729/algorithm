#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (25.35%)
# Likes:    883
# Dislikes: 0
# Total Accepted:    47.6K
# Total Submissions: 185.2K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#
#


# @lc code=start
class Solution:

    def isMatch_1(self, s: str, p: str) -> bool:
        # 1. 暴力递归
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch_1(s, p[2:]) or (first_match and self.isMatch_1(s[1:], p))
        else:
            return first_match and self.isMatch_1(s[1:], p[1:])

    def isMatch_2(self, s: str, p: str) -> bool:
        # 2. 带备忘录的递归
        # TODO:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)

            first = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or (first and dp(i + 1, j))
            else:
                ans = first and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        # 3. 动态规划
        # TODO:
        n = len(s)
        m = len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'

        for i in range(n):
            for j in range(m):
                if p[j] == s[i] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    if p[j - 1] != s[i]:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    if p[j - 1] == s[i] or p[j - 1] == ".":
                        dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j] or dp[i + 1][j - 1])

        return dp[-1][-1]


# @lc code=end

Solution().isMatch_2("aa", "a*")


# 1、匹配原始字符串：
def isMatch1(s, p):
    if not p:
        return not s
    first_match = bool(s) and p[0] == s[0]
    return first_match and isMatch1(s[1:], p[1:])


# 2、处理 . 通配符：
def isMatch2(s, p):
    if not p:
        return not s
    first_match = bool(s) and p[0] in {s[0], '.'}
    return first_match and isMatch2(s[1:], p[1:])


# 3、处理 * 通配符：
def isMatch3(s, p):
    if not p:
        return not s
    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        # * 表示 0 个时，匹配 s 和 p[2:]；* 表示多个时，匹配 p 和 s[1:]
        return isMatch3(s, p[2:]) or first_match and isMatch3(s[1:], p)
    else:
        return first_match and isMatch3(s[1:], p[1:])

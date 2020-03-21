#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
# https://leetcode-cn.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (30.91%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 17.6K
# Testcase Example:  '"aacecaaa"'
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
#
# 示例 1:
#
# 输入: "aacecaaa"
# 输出: "aaacecaaa"
#
#
# 示例 2:
#
# 输入: "abcd"
# 输出: "dcbabcd"
#
#


# @lc code=start
class Solution:

    def shortestPalindrome_1(self, s: str) -> str:
        # 1. 暴力法 ：先求出从头开始的最长子串
        # 判断是否回文：sub[::-1] == sub
        for i in range(len(s), -1, -1):
            sub = s[:i]
            if sub[::-1] == sub:
                break
        return s[i:][::-1] + s

    def shortestPalindrome(self, s: str) -> str:
        # TODO: 2. KMP(Knuth–Morris–Pratt)
        def compute_table(p):
            table = [0] * len(p)
            i = 1
            j = 0
            while i < len(p):
                if p[i] == p[j]:
                    j += 1
                    table[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = table[j - 1]
                    else:
                        i += 1
                        j = 0
            return table

        table = compute_table(s + "#" + s[::-1])
        return s[table[-1]:][::-1] + s


# @lc code=end

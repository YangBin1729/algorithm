#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (50.96%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 31.2K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
#
# 示例 1:
#
#
# 输入:
# "abccccdd"
#
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#
#
#


# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)

        res = 0
        i = 0
        for num in counts.values():
            if num % 2:
                i = 1
                res += num - 1
            else:
                res += num
        return res + i


# @lc code=end



#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (59.97%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    23.6K
# Total Submissions: 38.6K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。
#
#
#
# 示例:
#
# 输入：
# s = "abcd"
# t = "abcde"
#
# 输出：
# e
#
# 解释：
# 'e' 是那个被添加的字母。
#
#
#


# @lc code=start
class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        s = Counter(s)
        for char in t:
            if char in s and s[char] > 0:
                s[char] -= 1
            else:
                return char


# @lc code=end

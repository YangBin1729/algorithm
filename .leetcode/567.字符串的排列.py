#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (32.97%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    20.9K
# Total Submissions: 59.9K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#
#
# 示例2:
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
# 注意：
#
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
#
#


# @lc code=start
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        超时
        """
        if len(s1) > len(s2):
            return False

        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1

        window = {}
        for i in range(len(s1)):
            char = s2[i]
            window[char] = window.get(char, 0) + 1

        if window == target:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                window.pop(s2[i - len(s1)])
                
            window[s2[i]] = window.get(s2[i], 0) + 1
            if window == target:
                return True
        return False


# @lc code=end

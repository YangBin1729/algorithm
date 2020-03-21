#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (50.92%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 34K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom)
# 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true
# ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
#
# 注意：
#
# 你可以假设两个字符串均只含有小写字母。
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
#


# @lc code=start
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        counts = Counter(magazine)
        for char in ransomNote:
            if char not in counts:
                return False
            else:
                counts[char] -= 1
        return all(c >= 0 for char, c in counts.items())


# @lc code=end

#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (41.65%)
# Likes:    147
# Dislikes: 0
# Total Accepted:    73.8K
# Total Submissions: 175.2K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
#
#


# @lc code=start
class Solution:

    def isPalindrome_1(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True


    def isPalindrome(self, s: str) -> bool:
        # KEY：简洁！！
        s = list(filter(str.isalnum, s.lower()))
        return s == s[::-1]


# @lc code=end

s = "A man, a plan, a canal: Panama"
Solution().isPalindrome(s)
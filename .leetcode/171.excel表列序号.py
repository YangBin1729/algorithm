#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#
# https://leetcode-cn.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (65.81%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    32.9K
# Total Submissions: 49.4K
# Testcase Example:  '"A"'
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# 示例 1:
#
# 输入: "A"
# 输出: 1
#
#
# 示例 2:
#
# 输入: "AB"
# 输出: 28
#
#
# 示例 3:
#
# 输入: "ZY"
# 输出: 701
#
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。
#
#


# @lc code=start
class Solution:

    def titleToNumber(self, s: str) -> int:
        # import string
        # d = {char: num for num, char in enumerate(string.ascii_uppercase, 1)}

        res = 0
        n = len(s)
        for i in range(n):
            # res += 26**(n - 1 - i) * d[s[i]]
            # res = res * 26 + d[s[i]]
            res = res * 26 + ord(s[i]) - 64
        return res


# @lc code=end

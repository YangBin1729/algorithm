#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (35.79%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    20.9K
# Total Submissions: 56.6K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
# 例如，
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# 示例 1:
#
# 输入: 1
# 输出: "A"
#
#
# 示例 2:
#
# 输入: 28
# 输出: "AB"
#
#
# 示例 3:
#
# 输入: 701
# 输出: "ZY"
#
#
#

# @lc code=start


class Solution:

    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n:
            n, y = divmod(n, 26)
            if y == 0:
                n -= 1
                y = 26
            ans = chr(y + 64) + ans
        return ans


# @lc code=end

print(Solution().convertToTitle(701))
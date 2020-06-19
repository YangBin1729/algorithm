#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.61%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    19.8K
# Total Submissions: 46.4K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
#
# 输入：16
# 输出：True
#
# 示例 2：
#
# 输入：14
# 输出：False
#
#
#


# @lc code=start
class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        """
        1. 二分查找
        """
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def isPerfectSquare_2(self, num: int) -> bool:
        """
        2. 平方数一定可以写成 等差数列 之和：16=1+3+5+7
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


# @lc code=end

#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.24%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    80K
# Total Submissions: 214.7K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
#
#
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # TODO: 1. 牛顿迭代法

        # 2. 二分查找
        if x == 0: return 0
        left, right = 1, x // 2
        while left < right:
            mid = (left + right + 1) / 2
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        return left


# @lc code=end

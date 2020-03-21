#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (47.03%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    20.7K
# Total Submissions: 42.9K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
#
#
# 示例 2:
#
# 输入: 5
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#


# @lc code=start
class Solution:

    def isPowerOfFour(self, num: int) -> bool:
        # TODO 
        while num > 1:
            if num & 1 == 1:
                return False
            else:
                num = num >> 1
                if num & 1 == 1:
                    return False
                num = num >> 1
        return num == 1


# @lc code=end

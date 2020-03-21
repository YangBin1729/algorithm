#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode-cn.com/problems/single-number/description/
#
# algorithms
# Easy (64.35%)
# Likes:    1074
# Dislikes: 0
# Total Accepted:    152.3K
# Total Submissions: 232.7K
# Testcase Example:  '[2,2,1]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
#
#
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4
#
#

from typing import List


# @lc code=start
class Solution:

    def singleNumber_1(self, nums: List[int]) -> int:
        singles = []
        for num in nums:
            if num not in singles:
                singles.append(num)
            else:
                singles.remove(num)
        return singles.pop()


    def singleNumber_2(self, nums: List[int]) -> int:
        singles = {}
        for num in nums:
            try:
                singles.pop(num)
            except:
                singles[num] = 1
        return singles.popitem()[0]
    


    def singleNumber(self, nums: List[int]) -> int:
        """
        # KEY: 位操作：
        1. 异或满足交换律：a ^ b ^ c <=> a ^ c ^ b
        2. 任何数与 0 异或：0 ^ n = n
        3. 相同的数异或：n ^ n = 0 
        """
        a = 0
        for i in nums:
            a ^= i
        return a
    



# @lc code=end

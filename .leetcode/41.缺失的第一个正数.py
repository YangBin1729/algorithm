#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (37.02%)
# Likes:    411
# Dislikes: 0
# Total Accepted:    40.6K
# Total Submissions: 107.7K
# Testcase Example:  '[1,2,0]'
#
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
#
#
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
#
#
# 说明:
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
#
#

from typing import List


# @lc code=start
class Solution:

    def firstMissingPositive_1(self, nums: List[int]) -> int:
        """
        空间复杂度不符合要求！！
        """
        numSet = set(nums)
        max_num = max(numSet)

        if max_num <= 0:
            return 1
        else:
            for i in range(1, max_num):
                if i not in numSet:
                    return i
            else:
                return max_num + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        空间复杂度不符合要求！！
        TODO:
        """
        n = len(nums)
        




# @lc code=end

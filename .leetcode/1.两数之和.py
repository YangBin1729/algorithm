#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (47.06%)
# Likes:    7083
# Dislikes: 0
# Total Accepted:    714.1K
# Total Submissions: 1.5M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#
#
from typing import List


# @lc code=start
class Solution:

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        1. 暴力法， 两次遍历
        """
        n = len(nums)
        for i in range(n - 1):
            res = target - nums[i]
            for j in range(i + 1, n):
                if nums[j] == res:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        2. 哈希表，一次遍历
        KEY：将 数 及 余数的索引 作为键值对储存
        """

        nums_dict = dict()
        for i, num in enumerate(nums):
            if nums_dict.get(num) == None:
                nums_dict[target - num] = i
            else:
                return [nums_dict.get(num), i]


# @lc code=end

import math


def findContinuousSequence(target):
    res = []
    for n in range(int(math.sqrt(2 * target)) + 1, 1, -1):
        t, r = divmod(2 * target - n**2 + n, 2 * n)
        if r == 0 and t >= 1:
            res.append(list(range(t, t + n)))
    return res


print(findContinuousSequence(15))

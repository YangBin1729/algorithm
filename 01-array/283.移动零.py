#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

from typing import List

# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        1. 遍历，定义计数器 j 表征非零元素的个数
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        # 2. 排序
        # nums.sort(key=bool, reverse=True)                

# @lc code=end

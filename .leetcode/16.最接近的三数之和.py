#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (42.14%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    67.5K
# Total Submissions: 158.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#
from typing import List


# @lc code=start
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if abs(target - three_sum) < abs(target - ans):
                    ans = three_sum
                if three_sum > target:
                    k -= 1
                elif three_sum < target:
                    j += 1
                else:
                    return ans
        return ans


# @lc code=end

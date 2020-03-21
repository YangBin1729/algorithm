#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (24.65%)
# Likes:    1585
# Dislikes: 0
# Total Accepted:    127.2K
# Total Submissions: 516.2K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
from typing import List


# @lc code=start
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. 数组先排序为递增，
        2. 然后 i 遍历，同时内部双指针 j、k 指向 i+1、n-1；
           i+j+k>0，所以减小 k；i+j+k<0，所以增大 j；
           还要避免重复结果
        复杂度：时间——排序 O(nlogn)，遍历 O(n^2)，总共 O(n^2)；空间 O(1)
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while (j < k and nums[j] == nums[j + 1]):
                        j += 1
                    while (j < k and nums[k] == nums[k - 1]):
                        k -= 1
                    j += 1
                    k -= 1
                elif three_sum > 0:
                    k -= 1
                else:
                    j += 1
        return res


# @lc code=end

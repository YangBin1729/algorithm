#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (36.12%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 139.2K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
from typing import List


# @lc code=start
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        nums.sort()
        ans = []
        for i in range(n - 3):
            # 几个特殊情况的处理：
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                # 同理，特殊情况
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                a, b = j + 1, n - 1
                while a < b:
                    tmp = nums[i] + nums[j] + nums[a] + nums[b]
                    if tmp > target:
                        b -= 1
                    elif tmp < target:
                        a += 1
                    else:
                        ans.append([nums[i], nums[j], nums[a], nums[b]])
                        while a < b and nums[a] == nums[a + 1]:
                            a += 1
                        while a < b and nums[b] == nums[b - 1]:
                            b -= 1
        return ans


# @lc code=end

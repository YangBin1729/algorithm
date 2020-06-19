#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (32.24%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    24.6K
# Total Submissions: 75.9K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 说明:
#
# 假设你总是可以到达数组的最后一个位置。
#
#
from typing import List


# @lc code=start
class Solution:

    def jump(self, nums: List[int]) -> int:
        """
        1. 贪心算法：位置i可达的点 i+1~i+nums[i]，从中选择可以跳最远的那个点为下一点
        直观、且可直接记录下每次的跳跃点
        """
        jumps = 0
        i, n = 0, len(nums)
        if n <= 1:
            return jumps
        while i < n:
            j = i + nums[i]
            if j < n - 1:     # 选择 i+1 到 j 中可以跳最远的点为下一个 i
                i = max(range(i + 1, j + 1), key=lambda ind: ind + nums[ind])
                jumps += 1
            else:
                jumps += 1
                return jumps

    def jump_1(self, nums: List[int]) -> int:
        """
        2. 重构代码
        - curEnd 表示选择一个点后的可达边界，curMax 所有可达点中可以跳最远的那个点
            - 初始时：位于 0 处，curEnd=0
        - 在可达边界点内选择跳的最远的那一个，即每次达到边界处时，一定已经进行了一次选择
        """
        jumps = 0
        curEnd, curMax = 0, 0
        for i in range(len(nums) - 1):
            curMax = max(curMax, i + nums[i])
            if i == curEnd: # 可达范围中选择最大的哪一个，反过来到达边界处，必定已经进行了一次选择
                jumps += 1
                curEnd = curMax
        return jumps



# @lc code=end

nums = [2, 3, 1, 1, 4]
Solution().jump(nums)
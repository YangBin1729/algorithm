#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (59.75%)
# Likes:    945
# Dislikes: 0
# Total Accepted:    109.8K
# Total Submissions: 183.8K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#
#

from typing import List

# @lc code=start


class Solution:
    def maxArea_1(self, height: List[int]) -> int:
        """
        1. 暴力法，两层循环
        复杂度：时间 O(n^2) 空间 O(1)
        """
        n = len(height)
        max_area = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                max_area = max(area, max_area)
        return max_area

    def maxArea(self, height: List[int]) -> int:
        """
        2. 双指针 i、j，分别指向首尾，都向中间靠近。
        原理：循环时宽总在减少；改变 i、j 中较大者，最终高不变或减小，面积总减小；
             改变较小者，高可能增大，面积才可能增大；所以优先改变较小者。
        复杂度：时间 O(n) 空间 O(1)
        """
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                min_height = height[i]
                i += 1
            else:
                min_height = height[j]
                j -= 1
            area = (j - i + 1) * min_height
            max_area = max(area, max_area)
        return max_area


# @lc code=end

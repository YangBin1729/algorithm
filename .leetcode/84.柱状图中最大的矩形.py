#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (37.59%)
# Likes:    342
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 55.1K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
#
from typing import List


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 3. 栈     
        # # KEY：栈的巧妙应用！
        heights.append(0)
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            else:
                stack.append(i)
        return max_area

    def largestRectangleArea_2(self, heights: List[int]) -> int:
        # 1. 暴力，三层循环，**超时**
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                width = j - i + 1
                height = heights[i]
                for k in range(i, j + 1):
                    height = min(heights[k], height)
                max_area = max(max_area, width * height)

        return max_area

    def largestRectangleArea_3(self, heights: List[int]) -> int:
        # 2. 遍历，指针 i 对应的 height 表示矩形的高，然后指针 j、k 分别向两边遍历，**超时**
        max_area = 0
        for i in range(len(heights)):
            height = heights[i]
            j, k = i, i
            while j > 0 and heights[j - 1] >= height:
                j -= 1
            while k < len(heights) - 1 and heights[k + 1] >= height:
                k += 1
            width = k - j + 1
            max_area = max(height * width, max_area)
        return max_area

    def largestRectangleArea_4(self, heights: List[int]) -> int:
        # TODO：分治算法
        pass


# @lc code=end

heights = [2, 1, 5, 6, 2, 3]
max_area = Solution().largestRectangleArea(heights)
print(max_area)
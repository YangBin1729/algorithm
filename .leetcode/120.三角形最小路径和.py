#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (62.74%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    33K
# Total Submissions: 52.3K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
#
from typing import List
import copy

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nums  = copy.deepcopy(triangle)
        n = len(nums)
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                print(nums[i+1][j])
                nums[i][j] += min(nums[i+1][j], nums[i+1][j+1])
        return nums[0][0]

        
# @lc code=end

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Solution().minimumTotal(triangle)

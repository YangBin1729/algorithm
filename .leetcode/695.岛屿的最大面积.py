#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (58.74%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 34.5K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地)
# 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
#
# 示例 1:
#
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
#
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
#
# 示例 2:
#
#
# [[0,0,0,0,0,0,0,0]]
#
# 对于上面这个给定的矩阵, 返回 0。
#
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
#
#

from typing import List


# @lc code=start
class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        bfs
        TODO:优化
        """
        n, m = len(grid), len(grid[0])
        self.area = 0

        def bfs(i, j):
            grid[i][j] = 0
            self.area += 1
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_i, next_j = dx + i, dy + j
                if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j]:
                    bfs(next_i, next_j)

        area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    self.area = 0
                    bfs(i, j)
                    area = max(area, self.area)
        return area


# @lc code=end

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

grid = [[0,0,0,0,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
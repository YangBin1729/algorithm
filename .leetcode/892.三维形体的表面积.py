#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (55.11%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 14.2K
# Testcase Example:  '[[2]]'
#
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
#
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
#
# 请你返回最终形体的表面积。
#
#
#
#
#
#
# 示例 1：
#
# 输入：[[2]]
# 输出：10
#
#
# 示例 2：
#
# 输入：[[1,2],[3,4]]
# 输出：34
#
#
# 示例 3：
#
# 输入：[[1,0],[0,2]]
# 输出：16
#
#
# 示例 4：
#
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
#
#
# 示例 5：
#
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#
#
#
#
# 提示：
#
#
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
#
#
#

from typing import List


# @lc code=start
class Solution:

    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                area += 2     # 上下表面积
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    next_i, next_j = i + dx, j + dy
                    if 0 <= next_i < n and 0 <= next_j < n:
                        area += grid[i][j] - grid[next_i][next_j] if grid[i][j] > grid[next_i][
                            next_j] else 0
                    else:
                        area += grid[i][j]
        return area


# @lc code=end

grid = [[1, 0], [0, 2]]
print(Solution().surfaceArea(grid))

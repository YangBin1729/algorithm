#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (46.11%)
# Likes:    315
# Dislikes: 0
# Total Accepted:    45.7K
# Total Submissions: 98.6K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给定一个由 '1'（陆地）和
# '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3
#
#
#
from typing import List


# @lc code=start
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1. DFS：
        从 1 出发，遍历所有直达的 1 ，并将其标记；
        """
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = '#'
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nxt_i, nxt_j = i + dx, j + dy
                if 0 <= nxt_i < n and 0 <= nxt_j < m and grid[nxt_i][nxt_j] == '1':
                    dfs(nxt_i, nxt_j)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res

    def numIslands_2(self, grid: List[List[str]]) -> int:
        """
        2. BFS：
        队列实现
        """
        if not grid:
            return 0

        from collections import deque
        row, col = len(grid), len(grid[0])

        cnt = 0

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = "0"
            while queue:
                i, j = queue.popleft()
                for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                        grid[tmp_i][tmp_j] = "0"
                        queue.append((tmp_i, tmp_j))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i, j)
                    cnt += 1
        return cnt

    def numIslands_1(self, grid: List[List[str]]) -> int:
        # TODO: 二叉树，连续的可以按树的边一线连接的 1 为一个岛屿
        # FIXME: 速度太慢

        from collections import deque

        m = len(grid)
        if m == 0:
            return 0

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        for direction in directions:
                            # 访问上下左右节点，值为 1 ，且之前没被访问过的加入栈，用来继续搜索，并标记为 已访问。
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][
                                    new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                marked[new_i][new_j] = True
        return count

    def numIslands2(self, grid: List[List[str]]) -> int:
        # TODO: 并查集
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        if not grid:
            return 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    for x, y in [[1, 0], [0, 1]]:
                        next_i = i + x
                        next_j = j + y
                        if 0 <= next_i < row and 0 <= next_j < col and grid[next_i][
                                next_j] == "1":
                            union(next_i * col + next_j, i * col + j)
        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res.add(find((i * col + j)))
        return len(res)


# @lc code=end

grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]

print(Solution().numIslands2(grid))

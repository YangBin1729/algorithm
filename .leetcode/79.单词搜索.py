#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (39.47%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    32.2K
# Total Submissions: 80.8K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
#
#

from typing import List


# @lc code=start
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, n):
            if n == len(word):
                return True

            board[i][j] = '#'

            for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                if 0 <= i + dx < rows and 0 <= j + dy < cols and board[i + dx][j +
                                                                               dy] == word[n]:
                    if dfs(i + dx, j + dy, n + 1):
                        return True

            board[i][j] = word[n - 1]     # 状态还原

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True
        return False


# @lc code=end

board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
print(Solution().exist(board, 'ABCCEDAS'))

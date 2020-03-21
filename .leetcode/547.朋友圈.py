#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (53.78%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 40.4K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#
# 示例 1:
#
#
# 输入:
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
#
#
# 示例 2:
#
#
# 输入:
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
#
#
# 注意：
#
#
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
#
#
#
from typing import List


# @lc code=start
class Solution:

    def findCircleNum(self, M: List[List[int]]) -> int:
        # TODO: 并查集
        if not M:
            return 0
        n = len(M)

        def _union(p, i, j):
            p1 = _parent(p, i)
            p2 = _parent(p, j)
            p[p2] = p1

        def _parent(p, i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i
                i = p[i]
                p[x] = root
            return root

        # 索引 i 表示节点 i ，p[i] 表示该节点的根节点
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 1:
                    _union(p, i, j)
        return len(set([_parent(p, i) for i in range(n)]))

    def findCircleNum_2(self, M: List[List[int]]) -> int:
        """
        DFS
        """
        n = len(M)
        res = 0
        friends = set()

        def dfs(i):
            for row in range(n):
                if M[i][row] == 1 and row not in friends:
                    friends.add(row)
                    dfs(row)

        for i in range(n):
            if i not in friends:
                res += 1
                dfs(i)
        return res



# @lc code=end

M = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]

Solution().findCircleNum(M)


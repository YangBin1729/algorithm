#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
# https://leetcode-cn.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (47.39%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 3.5K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
#
# 假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
#
# 例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
#
# 与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
#
# 现在给定3个参数 — start, end,
# bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。
#
# 注意:
#
#
# 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
# 所有的目标基因序列必须是合法的。
# 假定起始基因序列与目标基因序列是不一样的。
#
#
# 示例 1:
#
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# 返回值: 1
#
#
# 示例 2:
#
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# 返回值: 2
#
#
# 示例 3:
#
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# 返回值: 3
#
#
#

from typing import List


# @lc code=start
class Solution:

    def minMutation1(self, start: str, end: str, bank: List[str]) -> int:
        """
        1. BFS：
        遍历基因库(bank)，保留能由当前序列(curr)合法变异得到的序列。
        """
        def validMutation(curr, next):
            return sum([c != n for c, n in zip(curr, next)]) == 1

        from collections import deque
        queue = deque([[start, 0]])
        explored = set()
        while queue:
            curr, mutations = queue.popleft()
            if curr == end:
                return mutations
            for s in bank:
                if validMutation(curr, s) and s not in explored:
                    queue.append([s, mutations + 1])
                    explored.add(s)
        return -1

    def minMutation2(self, start: str, end: str, bank: List[str]) -> int:
        """
        2. BFS：
        由当前序列(curr)生成所有可能的变异，遍历并判断是否为合法的变异。
        """
        from collections import deque
        queue = deque([[start, 0]])
        explored = set()
        while queue:
            curr, mutations = queue.popleft()
            if curr == end:
                return mutations
            for s in [curr[:i] + r + curr[i + 1:] for i in range(len(curr)) for r in 'ACGT']:
                if s in bank and s not in explored:
                    queue.append([s, mutations + 1])
                    explored.add(s)
        return -1


    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        3. 双向BFS
        """
        bank = set(bank)
        if end not in bank:
            return -1

        front, back = {start}, {end}
        changes = 0
        while front:
            changes += 1

            nxt_front = set()
            for s in front:
                for i in range(len(s)):
                    for c in 'ACGT':
                        nxt_s = s[:i] + c + s[i+1:]
                        if nxt_s != s:
                            if nxt_s in back:
                                return changes
                            if nxt_s in bank:
                                nxt_front.add(nxt_s)
                                bank.remove(nxt_s)
            
            front = nxt_front
            while len(front) > len(back):
                front, back = back, front 
        return -1 


# @lc code=end

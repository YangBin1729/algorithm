#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# https://leetcode-cn.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (41.11%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 12.9K
# Testcase Example:  '[[1,3],[0,2],[1,3],[0,2]]'
#
# 给定一个无向图graph，当这个图为二分图时返回true。
#
# 如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
#
#
# graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边：
# graph[i] 中不存在i，并且graph[i]中没有重复的值。
#
#
#
# 示例 1:
# 输入: [[1,3], [0,2], [1,3], [0,2]]
# 输出: true
# 解释:
# 无向图如下:
# 0----1
# |    |
# |    |
# 3----2
# 我们可以将节点分成两组: {0, 2} 和 {1, 3}。
#
#
#
#
# 示例 2:
# 输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
# 输出: false
# 解释:
# 无向图如下:
# 0----1
# | \  |
# |  \ |
# 3----2
# 我们不能将节点分割成两个独立的子集。
#
#
# 注意:
#
#
# graph 的长度范围为 [1, 100]。
# graph[i] 中的元素的范围为 [0, graph.length - 1]。
# graph[i] 不会包含 i 或者有重复的值。
# 图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def isBipartite_2(self, graph: List[List[int]]) -> bool:
        """
        将节点i和其连接点集graph[i]，依次添加到不同的两个集合，这两个集合不应该相交！
        TODO: 解答错误
        """
        A, B = set([0]), set(graph[0])
        i = 1
        while i < len(graph):
            if i in A or any(node in B for node in graph[i]):
                A.add(i)
                B.update(graph[i])
            # elif i in B or any(node in A for node in graph[i]):
            #     B.add(i)
            #     A.update(graph[i])
            else:
                # 当新的节点i和其连接点集graph[i] 和 A与B都没有交集时，i应该添加到A还是B？导致问题解答错误
                B.add(i)
                A.update(graph[i])
            i += 1
            if A & B:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        记录节点属于集合A还是集合B
        """
        states = {}
        for node in range(len(graph)):
            if node not in states:
                stack = [node]
                states[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in states: # 
                            stack.append(nei)
                            states[nei] = states[node] ^ 1
                        elif states[nei] == states[node]:     # 节点与其连接点必须在不同的结合
                            return False
        return True


# @lc code=end

graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(Solution().isBipartite(graph))

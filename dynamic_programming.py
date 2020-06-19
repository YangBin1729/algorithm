# __author__ = 'yangbin1729'
#
# ############################ 动态规划 ############################
# """
# ----DP 问题：
# 1.出现重叠子问题,并从子问题最优解推导出最优解
#     a.分治算法是将原始问题分解为无关的子问题
# 2.最优子结构
#     给定问题的最优解可以通过子问题的最优解获得
#
# ----动态规划与递归：
# 1.递归，从顶至底，可能导致同一个子问题被计算多次
# 2.动态规划，从底至顶，可能导致计算了很多不必要的子问题
#     a. 如杨辉三角的计算 C(n,m) = C(n-1,m) + C(n-1,m-1)
#     b. 动态规划必须计算整个三角，来获得 C(5，4)
# 3.对于非重叠子问题，两者以几乎相同的方式工作。
#
# ----DP 的两种解法：
# 1.Top-Down: Memoization
# 2.Bottom-up: Tabulation
#     a. 定义状态：
#         - 如将问题描述为 dp[x], dp[0]为基状态，即递归法中的递归出口；dp[n]为目标状态；
#     b. 定义状态转移方程：
#         - 状态 dp[i+1] 和前面 0~i 个状态的关系
#     c. 求解：
#         - 从最基础子问题 dp[0]，依次向上求解至 dp[n]
#     d. DP 背后是基于数学归纳的原理
#     e. 与动态规划互补的贪婪算法，是基于其它原理
#
# """
#
# ############################ 任意整数归一的最少步骤 ############################
# """
# 给定任意整数 n,可以三种操作：
# a)、n=n-1
# b)、n%2==0,n=n/2
# c)、n%3==0,n=n/3
#
# 1. 求将 n 变为 1 的最少步骤
# """
#
#
# def memo(f):
#     cache = {}
#
#     def wraps(*args):
#         if args not in cache:
#             cache[args] = f(*args)
#         return cache[args]
#
#     return wraps
#
#
# @memo
# def r(n):
#     if n == 1:
#         return 0
#     return min(1 + r(n - 1), 1 + r(n / 2) if n % 2 == 0 else float('inf'),
#                1 + r(n / 3) if n % 3 == 0 else float('inf'))
#
#
# def dp_r(n):
#     dp = [0] * (n + 1)
#     for i in range(2, n + 1):
#         dp[i] = min(1 + dp[i - 1],
#                     1 + dp[int(i / 2)] if i % 2 == 0 else float('inf'),
#                     1 + dp[int(i / 3)] if i % 3 == 0 else float('inf'))
#     return dp[n]
#
#
# def test():
#     for i in range(1, 100):
#         assert r(i) == dp_r(i)
#     print('test pass')
#
#
# """"
# 2. 带状态的算法，即保存每一步做出的选择
# """
#
#
# def dp_r2(n):
#     dp = [(0, '1')] * (n + 1)
#     for i in range(2, n + 1):
#         dp[i] = min((1 + dp[i - 1][0], dp[i - 1][1] + '<--({}-1)'.format(i)), (
#             1 + dp[int(i / 2)][0],
#             dp[int(i / 2)][1] + '<--({}/2)'.format(i)) if i % 2 == 0 else (
#             float('inf'), ''), (1 + dp[int(i / 3)][0],
#                                 dp[int(i / 3)][1] + '<--({}/3)'.format(
#                                     i)) if i % 3 == 0 else (float('inf'), ''))
#     return dp[n]
#
#
# @memo
# def r2(n):
#     if n == 1:
#         return 0, '1'
#     return min((1 + r2(n - 1)[0], r2(n - 1)[1] + '<--({}-1)'.format(n)), (
#         1 + r2(n / 2)[0],
#         r2(n / 2)[1] + '<--({}/2)'.format(n)) if n % 2 == 0 else (
#         float('inf'), ''), (1 + r2(n / 3)[0], r2(n / 3)[1] + '<--({}/3)'.format(
#         n)) if n % 3 == 0 else (float('inf'), ''))
#
#
# """
# 3.根据 dp 表求得状态
# """
#
#
# ############################ Fibonacci sequence ############################
# # Fibonacci sequence
# def fib1(n):
#     if n == 0 or n == 1:
#         return n
#     return fib1(n - 1) + fib1(n - 2)
#
#
# """
# 1.Memoization (Top Down):
#     额外的内存开销，需要储存所有函数的输入与输出
# """
#
#
# def memoize(f):
#     cache = {}
#
#     def wrapped(n):
#         if n not in cache:
#             cache[n] = f(n)
#         return cache[n]
#
#     return wrapped
#
#
# @memoize
# def fib2(n):
#     if n == 0 or n == 1:
#         return n
#     return fib2(n - 1) + fib2(n - 2)
#
#
# # lookup = [0]*(n+1)
# def fib(n, lookup):
#     # Base case
#     if n == 0 or n == 1:
#         lookup[n] = n
#
#         # If the value is not calculated previously then calculate it
#     if lookup[n] is None:
#         lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)
#
#         # return the value corresponding to that value of n
#     return lookup[n]
#
#
# """
# 2.Tabulation (Bottom Up):
#     迭代与缓存方法，自顶向下，事先并不确定迭代的次数；
#     但该函数迭代次数已知，利用该信息，自底向上的方法
# """
#
#
# def fib3(n):
#     if n == 0 or n == 1:
#         return n
#     num1, num2 = 0, 1
#     for i in range(2, n + 1):
#         fib_n = num1 + num2
#         num1 = num2
#         num2 = fib_n
#     return fib_n
#
#
# def fib4(n):
#     # array declaration
#     f = [0] * (n + 1)
#
#     # base case assignment
#     f[1] = 1
#
#     # calculating the fibonacci and storing the values
#     for i in range(2, n + 1):
#         f[i] = f[i - 1] + f[i - 2]
#     return f[n]
#

# ############################ 最大子集和 ############################
# """
# 从一组数据中选择非相邻的元素组成子组，使得其和最大；
# 选与不选的策略
# """
# import numpy as np
#
# arr = [1, 2, 4, 1, 7, 8, 3]
#
#
# def rec_opt(arr, i):
#     if i == 0:
#         return arr[0]
#     elif i == 1:
#         return max(arr[0], arr[1])
#     else:
#         A = rec_opt(arr, i - 2) + arr[i]  # 选择第 i 个元素
#         B = rec_opt(arr, i - 1)  # 不选择第 i 个元素
#         return max(A, B)
#
#
# def dp_opt(arr, i):
#     opt = np.zeros(len(arr))
#     opt[0] = arr[0]
#     opt[1] = max(arr[0], arr[1])
#     for i in range(2, len(arr)):
#         A = opt[i - 2] + arr[i]
#         B = opt[i - 1]
#         opt[i] = max(A, B)
#
#
# ############################ 是否存在子集和为特定数 ############################
# """
# 选与不选的策略
# """
# arr_2 = [3, 34, 4, 12, 5, 2]
# S = 9
#
#
# def rec_subset(arr, i, s):
#     if s == 0:
#         return True
#     elif i == 0:
#         return arr[0] == s
#     elif arr[i] > s:
#         return rec_subset(arr, i - 1, s)
#     else:
#         A = rec_subset(arr, i - 1, s - arr[i])  # 选择第 i 个元素
#         B = rec_subset(arr, i - 1, s)  # 不选择第 i 个元素
#         return A or B
#
#
# def dp_subset(arr, S):
#     subset = np.zeros((len(arr), S + 1), dtype=bool)
#     subset[:, 0] = True
#     subset[0, :] = False
#     for i in range(1, len(arr)):
#         for s in range(1, S + 1):
#             if arr[i] > s:
#                 subset[i, s] = subset[i - 1, s]
#             else:
#                 A = subset[i - 1, s - arr[i]]
#                 B = subset[i - 1, s]
#                 subset[i, s] = A or B
#     r, c = subset.shape
#     return subset[r - 1, c - 1]
#
#
# ############################ 最长递增子序列 ############################
# import numpy as np
#
#
# def LIS(X):
#     n = len(X)
#     L = [1] * n
#     for i in range(1, n):
#         # L[i] = max(1 + L[j] if X[i] > X[j] for j in range(i))
#         for j in range(i):
#             if X[i] > X[j] and L[i] < 1 + L[j]:
#                 L[i] = 1 + L[j]
#     return L
#
#
# def LIS_solutions(X):
#     n = len(X)
#     L = [1] * n
#     state = [[i] for i in X]
#
#     for i in range(1, n):
#         # L[i] = max(1 + L[j] if X[i] > X[j] for j in range(i))
#         for j in range(i):
#             if X[i] > X[j] and L[i] < 1 + L[j]:
#                 L[i] = 1 + L[j]
#                 state[i] = state[j] + [X[i]]
#     return L, state
#
#
# # todo:找出的最长递增子序列并不完全
#
#
# ############################ todo:遍历所有点的最短路径 ############################
#
#
# import math
#
#
# def distance(a, b):
#     return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
#
#
# def shortest_path(points, start):
#     if len(points) == 1:
#         return distance(points[0], start), [points[0], start]
#
#     solutions = []
#     for x in points:
#         current = distance(x, start)
#         t = points.copy()
#         t.remove(x)
#         rest, pathes = shortest_path(t, x)
#         solutions.append((current + rest, pathes + [start]))
#     return min(solutions, key=lambda s: s[0])
#
#
# points = [(1, 0), (1, 1), (0, 1), (0.5, 0.5), (2, 0), [-1, -1]]
# start = (0, 0)
#
#
# def shortestPath(graph, u, v, k):
#     V = 4
#     INF = 999999999999
#
#     # Base cases
#     if k == 0 and u == v:
#         return 0
#     if k == 1 and graph[u][v] != INF:
#         return graph[u][v]
#     if k <= 0:
#         return INF
#
#     # Initialize result
#     res = INF
#
#     # Go to all adjacents of u and recur
#     for i in range(V):
#         if graph[u][i] != INF and u != i and v != i:
#             rec_res = shortestPath(graph, i, v, k - 1)
#             if rec_res != INF:
#                 res = min(res, graph[u][i] + rec_res)
#     return res
#
#
# def C(i, S):
#     # 表示终点为 i 时的最优路径
#     if not S:
#         return 0
#     return min(dis(i, j) + cost(j, S - {j}) for j in S)
#
#
# def dp(G):
#     n = G.number_of_nodes()
#     T = [[float('inf')] * (1 << n) for _ in range(n)]
#     # T[i][k] = C(i,k), 表示 k 对应的点子集， i 表示终点，时的最短路径
#
#     T[0][1] = 0
#     # C(0, {0}) 表示只有起点
#
#     for s in range(1 << n):
#         if sum(((s >> j) & 1) for j in range(n)) <= 1 or not (s & 1):
#             # x & 1 表示 x 的比特数的最后一位
#             # s >> j 表示 s 的比特数右移 j 位，即删除后 j 位
#             # (s >> j) & 1) for j in range(n) 表示 s 的比特数的每一位
#             # s 代表的集合必须含有2个及以上元素
#             # s & 1：s 比特位最后一位为 1， 即所代表的集合必须含有起点 0
#             continue
#
#         for i in range(1, n):
#             if not ((s >> i) & 1):
#                 # 元素 i 不在 s 表示的集合内
#                 continue
#             for j in range(n):
#                 if j == i or not ((s >> j) & 1):
#                     # 元素 j 不能等于 i， 且必须包含在集合 s 中
#                     continue
#
#                 T[i][s] = min(T[i][s], T[j][s ^ (1 << i)] + G[i][j]['weight'])
#     return min(T[i][(1 << n) - 1] + G[0][i]['weight'] for i in range(1, n))
#
#
# """模拟退火法
# https://ericphanson.com/blog/2016/the-traveling-salesman-and-10-lines-of-python/"""
# import random, numpy, math, copy, matplotlib.pyplot as plt
#
# cities = [random.sample(range(100), 2) for x in range(15)];
# tour = random.sample(range(15), 15);
#
# for temperature in numpy.logspace(0, 5, num=100000)[::-1]:
#     [i, j] = sorted(random.sample(range(15), 2));
#     newTour = tour[:i] + tour[j:j + 1] + tour[i + 1:j] + tour[i:i + 1] + tour[
#                                                                          j + 1:];
#     oldDistances = sum([math.sqrt(sum(
#         [(cities[tour[(k + 1) % 15]][d] - cities[tour[k % 15]][d]) ** 2 for d in
#          [0, 1]])) for k in [j, j - 1, i, i - 1]])
#     newDistances = sum([math.sqrt(sum(
#         [(cities[newTour[(k + 1) % 15]][d] - cities[newTour[k % 15]][d]) ** 2
#          for d in [0, 1]])) for k in [j, j - 1, i, i - 1]])
#     if math.exp((oldDistances - newDistances) / temperature) > random.random():
#         tour = copy.copy(newTour);
# plt.plot([cities[tour[i % 15]][0] for i in range(16)],
#          [cities[tour[i % 15]][1] for i in range(16)], 'xb-');
# plt.show()
#
# ############################ todo:两点间的最短路径 ############################
# """
# Dijkstra 算法：
#     a. 给定点作为源，通过所有数据点的最短路径
#     b. 两个集合，一个集合包含最短路径中的所有点，令一个集合包含其它所有点
# """
# import sys
#
#
# class Graph():
#
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)] for row in
#                       range(vertices)]
#
#     def printSolution(self, dist):
#         print("Vertex tDistance from Source")
#         for node in range(self.V):
#             print(node, "t", dist[node])
#
#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minDistance(self, dist, sptSet):
#
#         # Initilaize minimum distance for next node
#         min = sys.maxint
#
#         # Search not nearest vertex not in the
#         # shortest path tree
#         for v in range(self.V):
#             if dist[v] < min and sptSet[v] == False:
#                 min = dist[v]
#                 min_index = v
#
#         return min_index
#
#         # Funtion that implements Dijkstra's single source
#
#     # shortest path algorithm for a graph represented
#     # using adjacency matrix representation
#     def dijkstra(self, src):
#
#         dist = [sys.maxint] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V
#
#         for cout in range(self.V):
#
#             # Pick the minimum distance vertex from
#             # the set of vertices not yet processed.
#             # u is always equal to src in first iteration
#             u = self.minDistance(dist, sptSet)
#
#             # Put the minimum distance vertex in the
#             # shotest path tree
#             sptSet[u] = True
#
#             # Update dist value of the adjacent vertices
#             # of the picked vertex only if the current
#             # distance is greater than new distance and
#             # the vertex in not in the shotest path tree
#             for v in range(self.V):
#                 if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > \
#                         dist[u] + self.graph[u][v]:
#                     dist[v] = dist[u] + self.graph[u][v]
#
#         self.printSolution(dist)
#
#
# ############################ 70.爬楼梯 ############################
#
# def climb_stairs(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         A = climb_stairs(n - 1)
#         B = climb_stairs(n - 2)
#     return A + B
#
#
# def dp_climb_stairs(n):
#     opt = [0] * (n + 1)
#     opt[0] = 1
#     opt[1] = 1
#     for i in range(2, n + 1):
#         opt[i] = opt[i - 1] + opt[i - 2]
#     return opt[n]
#
#
# def dp_climb_stairs_2(n):
#     a, b = 1, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
#
# ############################ 746.使用最小花费爬楼梯 ############################
# # todo
# def minCostClimbingStairs(cost):
#     n = len(cost)
#     if n == 1:
#         return cost[0]
#     elif n == 2:
#         return min(cost)
#     else:
#         A = cost[n - 1] + minCostClimbingStairs(cost[:n - 2])
#         B = minCostClimbingStairs(cost[:n - 1])
#         return min(A, B)
#
#
# def dp_minCostClimbingStairs(cost):
#     n = len(cost)
#     opt = [0] * n
#     opt[0] = cost[0]
#     opt[1] = cost[1]
#     for i in range(2, n):
#         opt[i] = min(opt[i - 2], opt[i - 1]) + cost[i]
#     return opt[n - 1]
#
#
# def minCostClimbingStairs(cost):
#     n = len(cost)
#     if n == 2:
#         return min(cost)
#
#     p = cost[0]
#     q = cost[1]
#     for i in range(2, n):
#         next_ = min(p, q) + cost[i]
#         p = q
#         q = next_
#     return min(p, q)

############################ LeetCode：5. 最长回文子串 ############################
def longestPalindrome(s):
    """
    1. dp[i][j] 表示 s[j:i+1] 是否为回文子串
    2. 状态转移方程：
        - i==j: dp[i][j]=1
        - i-j==1 且 s[i]==s[j]： dp[i][j]=1
        - i-j>1 且 s[i]==s[j] 且 s[j+1:i] 为回文子串，即 dp[i-1][j+1]==1 时：
            dp[i][j]=1
    """
    res = ''
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, -1, -1):
            if s[i] == s[j] and (i - j <= 2 or dp[i - 1][j + 1] == 1):
                dp[i][j] = 1
                res = max(res, s[j:i + 1], key=len)
    return res


############################ LeetCode：32. 最长有效括号 ############################
def longestValidParentheses(s):
    """
    数组 dp，dp[i] 表示以 s[i] 结尾的最长有效括号：
    形如...() ：dp[i] = dp[i-2]+2
    形如...)) ：找到 dp[i-1] 的长度，s[i] 和 第 i-dp[i-1]-1 个元素匹配时

    """
    dp = [0] * len(s)
    res = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2 if i > 2 else 2
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                # KEY：状态转移方程！！
                dp[i] = dp[i - 1] + 2 + (
                    dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
            res = max(res, dp[i])
    return res


# ss = [")()())", "()(()())"]

############################ LeetCode：44. 通配符匹配 ############################
def isMatch(s, p):
    """
    1. dp[i][j] 表示 s 前 i 个字符和 p 的前 j 个字符是否匹配
    2. 转移方程：
        - s[i]=p[j] and dp[i-1][j-1]=True：   dp[i][j]=True
        - p[j]='?'，可以匹配任意单字符，且 dp[i-1][j-1]=True:    dp[i][j]=True
        - p[j]='*'，匹配空字符串，且 dp[i][j-1]=True:    dp[i][j]=True
                    匹配任意长字符串时，且 dp[i-1][j]=True:    dp[i][j]=True
    3. 初始状态：s 和 p 前面添加相同的占位符 ' '
    """
    n = len(s)
    m = len(p)
    
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    dp[0][0] = True
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    return dp[-1][-1]


s = "aa"
p = "*"
print(isMatch(s, p))


############################ LeetCode：72. 编辑距离 ############################
def numDistance(word1, word2):
    """
    1. dp[i][j] 表示 word1 的前 i 个字符和 word2 的前 j 个字符间的编辑距离
    2. 转移方程：
        - word1[i] 与 word2[j] 相同时 dp[i][j]=dp[i-1][j-1]
        - 否者：删除 word1[i] , dp[i-1][j]+1
               添加操作 dp[i][j-1]+1
               将 word1[i] 替换成 word2[j], dp[i-1][j-1]+1
               上述中最小者
    3. 初始状态：在 word1 和 word2 前添加相同的占位符
        dp[0][j] = j; d[i][0] = i
    """
    n, m = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + 1
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1,
                               dp[i][j - 1] + 1)
    return dp[-1][-1]


############################ LeetCode：85. 最大矩形 ############################
def maximalRectangle(matrix):
    res = 0
    dp = [[0] * len(matrix[0]) for _ in
          range(len(matrix))]  # dp[i][j] 表示 j 左边到 j 处连续的 "1" 的个数
    
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            if matrix[i][j] == '0':
                continue
            
            width = dp[i][j] = dp[i][j - 1] + 1 if j >= 1 else 1
            # 遍历每一行的第 j 列, 计算面积
            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                h = i - k + 1
                res = max(res, width * h)
    
    return res


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]


############################ LeetCode：91. 解码方法 ############################
def numDecodings(s):
    """
    dp[i] 表示 s 前 i 个字符的编码方式；
    状态转移方程，关键是 k= s[i-1:i+1] 这两个字符的状态！！
    """
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [1] * n
    for i in range(1, n):
        key = int(s[i - 1:i + 1])
        
        if key == 10 or key == 20:
            dp[i] = dp[i - 2] if i >= 2 else 1
        elif key in range(30, 100, 10) or key == 0:
            return 0
        elif 0 < key < 10 or key > 26:
            dp[i] = dp[i - 1]
        else:
            dp = dp[i - 1] + dp[i - 2] if i >= 2 else 2
    return dp[-1]


############################ LeetCode：115. 不同的子序列 ############################
def numDistinct(s, t):
    """
    1. s 和 t 开头都补上个占位符，如 * 号
    2. dp[i][j] 表示 t 的前 i 个 和 s 的前 j 个字符间的不同子序列
    3. 初始化：
        dp[0][j] 表示字符串 '*'+s[:j] 中含有子串 '*' 的个数
    4. 转移方程：
        s[j-1]!=t[i-1] 时意味着：s[j-1] 不能参与组成子序列，dp[i][j] = dp[i][j-1]
        s[j-1]=t[i-1] 时意味着：
            - 利用 s[j-1] 匹配 t[i-1]，有  dp[i-1][j-1] 种
            - 不利用 s[j-1] 时， 有 dp[i][j-1] 种
    """
    n, m = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for j in range(n + 1):
        dp[0][j] = 1
    
    for i in range(1, m + 1):
        for j in range(i, n + 1):
            if s[j - 1] != t[i - 1]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    
    return dp[-1][-1]


S = "babgbag"
T = "bag"


# print(numDistinct(S, T))

############################ LeetCode：300. 最长上升子序列 ############################
def lengthOfLIS(nums):
    dp = [1] * len(nums)  # dp[i] 表示以 nums[i] 结尾的最长上升子序列
    res = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    return res


# nums = [10, 9, 2, 5, 3, 7, 101, 18]

############################ LeetCode：818. 赛车 ############################
def racecar(target):
    """
    1. 连续 A（加速）指令 k 次后，位置依次为：1,3,7,15,31,63,127,255,511,1023 即：2^k-1
    2. 因此当 target = 2^k - 1 时，需要指令数 k
    3. target 位于 k 与 k+1 次指令位置中间时：
        1. 先超过 target 移动到 2^k-1 处再返回，此时剩下距离 res = 2^k-1-i，
           所需步骤为 dp[res]，总指令数：k + 1 + dp[res]
        2. 或者先移动到 2^(k-1) 处，指令数 k-1；再 R（倒车）并加速 j 次，此时剩余距离
           res = i- (2^（k-1)）+ 2^j；总指令数为 k-1 + 1+j+1 + dp[res];
           j 遍历 0~k-1，求出最小值
        3. 上述两种方案中较小者
    
    4. 初始条件：
    """
    
    # 初始条件：
    dp = [0, 1, 4] + [float('inf')] * target
    
    for t in range(3, target + 1):
        k = t.bit_length()
        
        # 在 2^k-1 处
        if t == 2 ** k - 1:
            dp[t] = k
            continue
        
        # 移动到 2^(k-1)-1 处，倒车，然后反方向依次运行 j 次
        res = t - (2 ** (k - 1) - 1)
        for j in range(k - 1):
            dp[t] = min(dp[t], k - 1 + 1 + j + 1 + dp[
                res + 2 ** j - 1])  # A*(k-1) + R + A*(j) + R
        
        # 移动到 2^k-1 处
        res = 2 ** k - 1 - t
        dp[t] = min(dp[t], k + 1 + dp[res])
    return dp[target]


racecar(5)


############################ LeetCode：1143. 最长公共子序列 ############################
def LCS(X, Y):
    n, m = len(X), len(Y)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j + 1][k + 1] = L[j][k] + 1
            else:
                L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])
    return L


def LCS_solution(X, Y):
    L = LCS(X, Y)
    
    solution = []
    j, k = len(X), len(Y)
    while L[j][k] > 0:
        if X[j - 1] == Y[k - 1]:
            solution.append(X[j - 1])
            j -= 1
            k -= 1
        elif L[j - 1][k] >= L[j][k - 1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))


############################ 背包问题 ############################

def simple_KnapSack(wts, max_wt):
    """
    :param wts: 可选物品的质量
    :param max_wt: 背包总质量
    :return: 返回可以选择的最大重量
    辅助数组 dp[i][w] 储存布尔值，表征对第 i 个物品做选择时，已选物品的总重量是否能为 w
    """
    dp = [[0] * (max_wt + 1) for _ in range(len(wts))]
    
    dp[0][0] = 1
    if wts[0] < max_wt:
        dp[0][wts[0]] = 1
    
    for i in range(1, len(wts)):
        for w in range(max_wt + 1):
            if dp[i - 1][w] == 1:  # 不选第 i 个物品
                dp[i][w] = 1
            elif w - wts[i] >= 0 and dp[i - 1][w - wts[i]] == 1:  # 选第 i 个物品
                dp[i][w] = 1
    
    print(dp)
    
    for w in range(max_wt, -1, -1):
        if dp[-1][w] == 1:
            return w
    
    return 0


def simple_KnapSack2(wts, max_wt):
    """
    上述解法中，求 i 层的值，只需要 i-1 层的结果；可将 dp 转换成一维
    """
    dp = [0] * (max_wt + 1)
    
    dp[0] = 1
    if wts[0] < max_wt:
        dp[wts[0]] = 1
    
    for i in range(1, len(wts)):
        for w in range(max_wt + 1):
            if w - wts[i] >= 0 and dp[w - wts[i]] == 1:  # 选第 i 个物品
                dp[i][w] = 1
    
    print(dp)
    
    for w in range(max_wt, -1, -1):
        if dp[w] == 1:
            return w
    
    return 0


def knapSack(max_wt, wts, vals):
    """
    :param max_wt: 背包总质量
    :param wts: 可选物品的质量
    :param vals: 物品对应的价值
    :return: 返回最大价值
    辅助数组 dp[i][w] 储存对第 i 个物品做选择时，已选物品的最大总价值

    """
    dp = [[-1] * (max_wt + 1) for _ in range(len(wts))]
    
    dp[0][0] = 0
    if wts[0] < max_wt:
        dp[0][wts[0]] = vals[0]
    
    for i in range(1, len(wts)):
        for w in range(max_wt + 1):
            if dp[i - 1][w] != -1:  # 不选第 i 个物品
                dp[i][w] = dp[i - 1][w]
        
        for w in range(max_wt + 1):
            if w - wts[i] >= 0 and dp[i - 1][w - wts[i]] != -1:  # 选第 i 个物品
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wts[i]] + vals[i])
    
    print(dp)
    res = 0
    for w in range(max_wt, -1, -1):
        res = max(dp[-1][w], res)
    
    return res


def knapSack2(max_wt, wts, vals):
    """
    :param max_wt: 背包总质量
    :param wts: 可选物品的质量
    :param vals: 物品对应的价值
    :return: 返回最大价值
    优化辅助数组占用的空间

    """
    dp = [-1] * (max_wt + 1)
    
    dp[0][0] = 0
    if wts[0] < max_wt:
        dp[wts[0]] = vals[0]
    
    for i in range(1, len(wts)):
        for w in range(max_wt + 1):
            if w - wts[i] >= 0 and dp[w - wts[i]] != -1:  # 选第 i 个物品
                dp[w] = max(dp[w], dp[w - wts[i]] + vals[i])
    
    print(dp)
    res = 0
    for w in range(max_wt, -1, -1):
        res = max(dp[w], res)
    
    return res


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapSack(W, wt, val))


def knapSack_solution(dp, wts, vals):
    """
    :param max_wt:
    :param wts:
    :param vals:
    :return: 返回选择的物品的列表？？？
    1. dp 中增加一个参数表征是否选择了第 i 个物品
    2. dp 增加一个维度，n*2*m，2*m 一行表示选择第 i 个物品，另一行表示不选择
    """
    # TODO
    i = len(dp) - 1
    
    j = 0
    for j in range(len(dp[0]) - 1, -1, -1):
        if dp[-1][j] != -1:
            break
    
    res = []
    while i >= 0 and j >= 0:
        if dp[i][j] != -1 and dp[i][j] == dp[i - 1][j - wts[i]] + vals[i]:
            res.append(i)
            j = j - wts[i]
        i -= 1
    print(res)
    return res


############################ 钢条切割问题 ############################
from collections import defaultdict

called_time = defaultdict(int)


def get_call_times(f):
    def wraps(n):
        result = f(n)
        called_time[(f.__name__, n)] += 1
        return result
    
    return wraps


@get_call_times  # 检查各个子函数被重复递归调用的次数
def cut_rod(p, n):
    """
    :param p: 为钢条长度与价值组成的词典
    :param n: 钢条总长度
    :return:
    """
    return max(
        [p[n]] + [cut_rod(p, i) + cut_rod(p, n - i) for i in range(1, n)])


from functools import wraps     # 备忘录


def memo(f):
    already_computed = {}
    
    @wraps(f)
    def _wrap(arg):
        result = None
        if arg in already_computed:
            result = already_computed[arg]
        else:
            result = f(arg)
            already_computed[arg] = result
        return result
    
    return _wrap

@memo  # 带备忘录的递归解法
def cut_rod(p, n):
    """
    :param p: 为钢条长度与价值组成的词典
    :param n: 钢条总长度
    :return:
    """
    return max(
        [p[n]] + [cut_rod(p, i) + cut_rod(p, n - i) for i in range(1, n)])


def MEMOIZED_cut_rod(p, n):
    """
    :param p: 为钢条长度与价值组成的词典
    :param n: 钢条总长度
    :return:
    """
    r = [-float('inf')] * (n + 1)
    
    def helper(p, n, r):
        if r[n] >= 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = -float('inf')
            for i in range(1, n + 1):
                q = max(q, p[i] + helper(p, n - i, r))
        r[n] = q
        return q
    
    return helper(p, n, r)


def BOTTOM_UP_cut_rod(p, n):
    r = [-float('inf')] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def cut_rod_helper(p, n):
    """
    s[j] 保存长度为 j 的钢条，最优切割方案中的第一段钢条的切割长度
    """
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
                r[j] = q
    return r, s


def print_cutRod_solution(p, n):
    r, s = cut_rod_helper(p, n)
    print(s)
    while n > 0:
        print(s[n])
        n = n - s[n]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 26]
n = 10
print_cutRod_solution(p, 7)
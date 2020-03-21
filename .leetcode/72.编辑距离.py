#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (55.26%)
# Likes:    457
# Dislikes: 0
# Total Accepted:    23.7K
# Total Submissions: 42.6K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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



# @lc code=end

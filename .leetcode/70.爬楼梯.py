#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (47.34%)
# Likes:    736
# Dislikes: 0
# Total Accepted:    109K
# Total Submissions: 230.3K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#
#


# @lc code=start
class Solution:

    def climbStairs_1(self, n: int) -> int:
        """"
        1. 递推
        """
        f1, f2, res = 1, 1, 1
        for _ in range(1, n):
            res = f1 + f2
            f1, f2 = f2, res
        return res


    memo = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        """
        2.递归
        # 第 n 阶，可以通过 n-1 阶跨一步达到，也可以通过 n-2 阶跨两步达到
        # 所以路径数量，是前两者的路径数量之和
        """

        if n in self.memo:
            res = self.memo[n]
        else:
            a = self.climbStairs(n - 1)
            b = self.climbStairs(n - 2)
            res = self.memo[n] = a + b

        return res


# @lc code=end
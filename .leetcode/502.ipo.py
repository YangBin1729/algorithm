#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
# https://leetcode-cn.com/problems/ipo/description/
#
# algorithms
# Hard (37.57%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 6.4K
# Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
#
# 假设 力扣（LeetCode）即将开始其 IPO。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。
# 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
#
# 给定若干个项目。对于每个项目 i，它都有一个纯利润 Pi，并且需要最小的资本 Ci 来启动相应的项目。最初，你有 W
# 资本。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
#
# 总而言之，从给定项目中选择最多 k 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。
#
# 示例 1:
#
# 输入: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
#
# 输出: 4
#
# 解释:
# 由于你的初始资本为 0，你尽可以从 0 号项目开始。
# 在完成后，你将获得 1 的利润，你的总资本将变为 1。
# 此时你可以选择开始 1 号或 2 号项目。
# 由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
# 因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
#
#
#
#
# 注意:
#
#
# 假设所有输入数字都是非负整数。
# 表示利润和资本的数组的长度不超过 50000。
# 答案保证在 32 位有符号整数范围内。
#
#
#
#
#

from typing import List


# @lc code=start
class Solution:

    def findMaximizedCapital(self, k: int, W: int, Profits: List[int],
                             Capital: List[int]) -> int:
        """
        贪心算法:在满足已有资本大于启动资本的条件下,优先选择利润大的项目
        TODO: 超时
        """
        indices = sorted(range(len(Profits)), key=lambda ind: -Profits[ind])

        for _ in range(k):
            for j in indices:
                if W >= Capital[j]:
                    W += Profits[j]
                    Capital[j] = float('inf') # 第 j 个项目已选
                    break
        return W


# @lc code=end

k = 2
W = 0
Profits = [1, 2, 3]
Capital = [0, 1, 1]
print(Solution().findMaximizedCapital(k, W, Profits, Capital))
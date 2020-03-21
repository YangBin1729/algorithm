#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (39.71%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    18.3K
# Total Submissions: 45.6K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#
# 示例 3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
#
#
from typing import List


# @lc code=start
class Solution:

    def maxProfit_1(self, prices: List[int]) -> int:
        """
        FIXME: 超时
        动态规划，辅助数组：
        dp[i][1] 表示前 i 天内 1 笔交易的最大利润
        dp[i][2] 表示前 i 天内 2 笔交易的最大利润
        - 第 i 天无动作， 则 dp[i][2] = dp[i-1][2]
        - 第 i 天卖出，则必须在第 j 天买入，此时利润 prices[i] - prices[j] + dp[j - 1][1]
        """
        if not prices:
            return 0

        dp = [[0] * (2 + 1) for _ in range(len(prices))]
        for k in range(1, 3):
            for i in range(1, len(prices)):
                temp = prices[i] - prices[0]     # 第 0 天买入、第 i 天售出时的收益
                for j in range(1, i):     # 第 j 天买入
                    temp = max(temp, prices[i] - prices[j] + dp[j - 1][k - 1])
                dp[i][k] = max(dp[i - 1][k], temp)     # 第 i 天不操作与第 i 天售出
        return dp[-1][-1]

    def maxProfit(self, prices: List[int]) -> int:
        """
        2. 找到中间的第 i 天 ==> 前 i 天的最大利润 + 后面的最大利润 --> max
        """
        if not prices:
            return 0

        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        print(profits)

        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(max_profit + profits[i], total_max)
        return total_max


# @lc code=end

prices = [3, 3, 5, 0, 0, 3, 1, 4]
Solution().maxProfit(prices)

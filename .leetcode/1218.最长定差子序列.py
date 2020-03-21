#
# @lc app=leetcode.cn id=1218 lang=python3
#
# [1218] 最长定差子序列
#
# https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
#
# algorithms
# Medium (33.02%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 6.1K
# Testcase Example:  '[1,2,3,4]\n1'
#
# 给你一个整数数组 arr 和一个整数 difference，请你找出 arr 中所有相邻元素之间的差等于给定 difference
# 的等差子序列，并返回其中最长的等差子序列的长度。
#
#
#
# 示例 1：
#
# 输入：arr = [1,2,3,4], difference = 1
# 输出：4
# 解释：最长的等差子序列是 [1,2,3,4]。
#
# 示例 2：
#
# 输入：arr = [1,3,5,7], difference = 1
# 输出：1
# 解释：最长的等差子序列是任意单个元素。
#
#
# 示例 3：
#
# 输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
# 输出：4
# 解释：最长的等差子序列是 [7,5,3,1]。
#
#
#
#
# 提示：
#
#
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i], difference <= 10^4
#
#
#

from typing import List


# @lc code=start
class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        动态规划：dp[i] 表示以 arr[i] 元素结尾的最长等差序列
        """
        n = len(arr)
        dp = [1] * n
        res = 1

        for i in range(1, n):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])

        print(dp)
        print(res)
        return res


# @lc code=end

Solution().longestSubsequence([1, 3, 5, 7], 1)

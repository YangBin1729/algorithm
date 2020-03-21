#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.58%)
# Likes:    133
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 18.1K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
# 示例 1:
#
#
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释:
# 长度最长的公共子数组是 [3, 2, 1]。
#
#
# 说明:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#

from typing import List


# @lc code=start
class Solution:

    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        动态规划
        dp[i][j] 表示以 A[i-1]/B[j-1] 结尾的最长子数组
        """
        n = len(A)
        m = len(B)

        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        
        return res


# @lc code=end

A = [0, 1, 1, 1, 1]
B = [1, 0, 1, 0, 1]
print(Solution().findLength(A, B))

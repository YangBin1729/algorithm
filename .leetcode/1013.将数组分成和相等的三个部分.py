#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#
# https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (52.59%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 26.7K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# 给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... +
# A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
#
#
#
# 示例 1：
#
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#
# 示例 2：
#
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
#
#
# 示例 3：
#
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
#
#
# 提示：
#
#
# 3 <= A.length <= 50000
# -10^4 <= A[i] <= 10^4
#
#
#

from typing import List


# @lc code=start
class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        """
        三个部分都是 A 连续的子数组
        """
        s = sum(A)
        if s % 3 != 0:
            return False

        target = s // 3
        n, i, cur = len(A), 0, 0
        while i < n:
            cur += A[i]
            if cur == target:
                break
            i += 1
        if cur != target:
            return False

        j = i + 1
        while j + 1 < n:
            cur += A[j]
            if cur == target * 2:
                return True
            j += 1
        return False


# @lc code=end

A = [18,12,-18,18,-19,-1,10,10]
Solution().canThreePartsEqualSum(A)
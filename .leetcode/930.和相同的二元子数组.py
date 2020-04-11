#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (33.46%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 6.9K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。
#
#
#
# 示例：
#
# 输入：A = [1,0,1,0,1], S = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
#
#
# 提示：
#
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] 为 0 或 1
#
#
#

from typing import List


# @lc code=start
class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        """
        TODO: 滑动窗口
        """
        n = len(A)
        i, j = 0, 1
        tmp = A[0] + A[1]
        res = 0
        while j < n:
            if tmp < S:
                j += 1
                tmp += A[j]
            elif tmp == S:
                res += 1
                j += 1
                while j < n and A[j] == 0:
                    j += 1
                    res += 1
                tmp += 1
            else:
                tmp -= A[i]
                i += 1
        return res


# @lc code=end

A = [1, 0, 1, 0, 1]
S = 2
# print(Solution().numSubarraysWithSum(A, S))



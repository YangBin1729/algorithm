#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (46.84%)
# Likes:    264
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 60.9K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
#

from typing import List


# @lc code=start
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            currLen = 1
            while num + 1 in numSet:
                currLen += 1
                num += 1
            res = max(res, currLen)
        return res


# @lc code=end

import random
nums = [random.randint(0, 1000) for _ in range(10000)]
import profile

profile.run("Solution().longestConsecutive(nums)")

#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.34%)
# Likes:    1844
# Dislikes: 0
# Total Accepted:    119.2K
# Total Submissions: 328K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#
from typing import List


# @lc code=start
class Solution:

    def findMedianSortedArrays_1(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. 归并排序的合并部分！！！O(n+m)
        # 额外的 O(n+m) 空间
        i = j = 0
        n1, n2 = len(nums1), len(nums2)

        k = 0
        s = [0] * (n1 + n2)
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                s[k] = nums1[i]
                i += 1
            else:
                s[k] = nums2[j]
                j += 1
            k += 1
        if i < n1:
            s[k:] = nums1[i:]
        if j < n2:
            s[k:] = nums2[j:]
        return s[(n1 + n2) //
                 2] if (n1 + n2) % 2 else (s[(n1 + n2) // 2] + s[(n1 + n2) // 2 - 1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO：


# @lc code=end

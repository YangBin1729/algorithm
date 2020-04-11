#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (45.87%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    94.9K
# Total Submissions: 206.1K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#
#

from typing import List


# @lc code=start
class Solution:

    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        1. 双指针，从左向右，需要额外的辅助数组
        """
        nums1_copy = nums1[:]

        i, j = 0, 0
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1[i + j] = nums1_copy[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1
        if i == m:     # nums1 最大元素比 nums2 的小时，nums1 内元素选择完，剩下的都是 nums2 的元素
            nums1[i + j:] = nums2[j:]
        if j == n:
            nums1[i + j:] = nums1_copy[i:m]
            # nums2 最大元素比 nums1 的小时，nums2 内元素选择完，剩下的都是 nums1 的元素

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        2. 双指针：从右向左填充，不需要额外空间
        """
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]


# @lc code=end
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
Solution().merge(nums1, m, nums2, n)
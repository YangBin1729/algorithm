#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (39.59%)
# Likes:    441
# Dislikes: 0
# Total Accepted:    87.1K
# Total Submissions: 218.5K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
#
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
#
#
#
from typing import List


# @lc code=start
class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. 切片赋值
        """
        n = len(nums)
        nums[:k], nums[k:] = nums[n - k:], nums[:n - k]

    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        2. 暴力法：每次旋转一个元素
        O(n*k)，超时！！
        """
        while k > 0:
            prev = nums[-1]
            for i in range(len(nums)):
                tmp = nums[i]
                nums[i] = prev
                prev = tmp
            k -= 1

    def rotate_2(self, nums: List[int], k: int) -> None:
        """
        3. 环状替换：索引 i 处的元素移动到 （i+k)%n 处；
        特殊情况，形成环，而不能替换所有点：[0,1,2,3],k=2,0-->2-->0
        # KEY:
        """
        n = len(nums)
        k %= n
        if k == 0:
            return

        # 从第一个元素开始替换，cnt 记录替换的次数
        i = 0
        tmp = nums[i]
        cnt = 0
        
        while cnt < n:

            # 从 i 出发替换，直到返回到 i
            nxt = (i + k) % n
            while nxt != i:
                nums[nxt], tmp = tmp, nums[nxt]
                nxt = (nxt + k) % n
                cnt += 1
            nums[nxt] = tmp
            cnt += 1

            # 完成了整个从 i 的环形后，下一个 i
            i += 1
            tmp = nums[i]

# @lc code=end

nums = [0, 1, 2, 3]
print(Solution().rotate_2(nums, 1))

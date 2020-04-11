#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (42.99%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    22.1K
# Total Submissions: 51.2K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
#
# 提示：
#
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
#
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#
#

from typing import List


# @lc code=start
class Solution:

    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:
        # 1. 暴力遍历，求切片的最大值
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i:i + k]) for i in range(n - k + 1)]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: 2. 双端队列，保留连续 k 个数中递减的那几个，
        # KEY：双端队列的妙用！！！
        from collections import deque
        res = []
        queue = deque()

        for i in range(len(nums)):
            if i >= k and i - k == queue[0]:
                queue.popleft()
                # 连续 k 个数，都是递减的，最左边的数总是最大的

            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
                # 弹出比当前值小的队列中的元素
            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])

        return res


# @lc code=end

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

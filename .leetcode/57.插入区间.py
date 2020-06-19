#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (36.17%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    14K
# Total Submissions: 38.1K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
# 示例 1:
#
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
# 示例 2:
#
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        将新区间添加到列表中，排序后再合并
        """
        intervals = sorted(intervals + [newInterval], key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        # TODO 
        """
        i, n = 0, len(intervals)
        res = []
        # 找左边重合区域
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        tmp = [newInterval[0], newInterval[1]]
        # 找右边重合区域
        while i < n and newInterval[1] >= intervals[i][0]:
            tmp[0] = min(tmp[0], intervals[i][0])
            tmp[1] = max(tmp[1], intervals[i][1])
            i += 1
        res.append(tmp)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


# @lc code=end


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

print(Solution().insert(intervals, newInterval))
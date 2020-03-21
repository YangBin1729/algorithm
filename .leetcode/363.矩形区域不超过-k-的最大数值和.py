#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#
# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (31.89%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 4.9K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# 给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。
# 
# 示例:
# 
# 输入: matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出: 2 
# 解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
# 
# 
# 说明：
# 
# 
# 矩阵内的矩形区域面积必须大于 0。
# 如果行数远大于列数，你将如何解答呢？
# 
# 
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # TODO:
# @lc code=end


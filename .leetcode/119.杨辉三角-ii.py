#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (59.09%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    35.9K
# Total Submissions: 60.2K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#
from typing import List


# @lc code=start
class Solution:

    def getRow_1(self, rowIndex: int) -> List[int]:
        # 1. 按杨辉三角逐层递推
        if rowIndex == 0:
            return [1]

        res = [1, 1]
        for i in range(2, rowIndex + 1):
            tmp = [1] * (i + 1)
            for j in range(1, i):
                tmp[j] = res[j - 1] + res[j]
            res = tmp
        return res

    def getRow(self, rowIndex: int) -> List[int]:
        # KEY：O(k)
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
        return res


# @lc code=end

Solution().getRow(4)
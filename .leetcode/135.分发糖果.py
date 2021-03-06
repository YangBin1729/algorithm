#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode-cn.com/problems/candy/description/
#
# algorithms
# Hard (40.54%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 34.6K
# Testcase Example:  '[1,0,2]'
#
# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
#
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
#
#
# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
#
#
# 那么这样下来，老师至少需要准备多少颗糖果呢？
#
# 示例 1:
#
# 输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
#
#
# 示例 2:
#
# 输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
#
#

from typing import List


# @lc code=start
class Solution:

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        left = [1] * n
        for i in range(1, n):     # 比左边学生评分高的糖果多
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        right = [1] * n
        for i in range(n - 1, 0, -1):     # 比右边学生评分高的糖果多
            if ratings[i - 1] > ratings[i]:
                right[i - 1] = right[i] + 1

        candies = [max(l, r) for l, r in zip(left, right)] # 比左右两边都大

        return sum(candies)


# @lc code=end

ratings = [1, 0, 2]
print(Solution().candy(ratings))
#
# @lc app=leetcode.cn id=335 lang=python3
#
# [335] 路径交叉
#
# https://leetcode-cn.com/problems/self-crossing/description/
#
# algorithms
# Hard (30.33%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    1K
# Total Submissions: 3.3K
# Testcase Example:  '[2,1,1,2]'
#
# 给定一个含有 n 个正数的数组 x。从点 (0,0) 开始，先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，向东移动
# x[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
#
# 编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。
#
#
#
# 示例 1:
#
# ┌───┐
# │   │
# └───┼──>
# │
#
# 输入: [2,1,1,2]
# 输出: true
#
#
# 示例 2:
#
# ┌──────┐
# │      │
# │
# │
# └────────────>
#
# 输入: [1,2,3,4]
# 输出: false
#
#
# 示例 3:
#
# ┌───┐
# │   │
# └───┼>
#
# 输入: [1,1,1,1]
# 输出: true
#
#
#

from typing import List


# @lc code=start
class Solution:

    def isSelfCrossing(self, x: List[int]) -> bool:
        """
        暴力法：
        """
        visited = {(0, 0)}
        a, b = 0, 0

        direction_id = 0
        directions = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
        for j in x:
            da, db = directions[direction_id]
            for _ in range(j):
                a, b = a + da, b + db
                if (a, b) in visited:
                    return True
                else:
                    visited.add((a, b))
            direction_id = (direction_id + 1) % 4
        return False


# @lc code=end

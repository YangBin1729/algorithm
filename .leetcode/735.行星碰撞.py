#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#
# https://leetcode-cn.com/problems/asteroid-collision/description/
#
# algorithms
# Medium (36.53%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 16.1K
# Testcase Example:  '[5,10,-5]'
#
# 给定一个整数数组 asteroids，表示在同一行的行星。
#
# 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
#
#
# 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
#
# 示例 1:
#
#
# 输入:
# asteroids = [5, 10, -5]
# 输出: [5, 10]
# 解释:
# 10 和 -5 碰撞后只剩下 10。 5 和 10 永远不会发生碰撞。
#
#
# 示例 2:
#
#
# 输入:
# asteroids = [8, -8]
# 输出: []
# 解释:
# 8 和 -8 碰撞后，两者都发生爆炸。
#
#
# 示例 3:
#
#
# 输入:
# asteroids = [10, 2, -5]
# 输出: [10]
# 解释:
# 2 和 -5 发生碰撞后剩下 -5。10 和 -5 发生碰撞后剩下 10。
#
#
# 示例 4:
#
#
# 输入:
# asteroids = [-2, -1, 1, 2]
# 输出: [-2, -1, 1, 2]
# 解释:
# -2 和 -1 向左移动，而 1 和 2 向右移动。
# 由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。
#
#
# 说明:
#
#
# 数组 asteroids 的长度不超过 10000。
# 每一颗行星的大小都是非零整数，范围是 [-1000, 1000] 。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for star in asteroids:
            while ans and star < 0 < ans[-1]:
                if ans[-1] < -star:
                    ans.pop()
                    continue
                elif ans[-1] == -star:
                    ans.pop()
                break
            else:
                ans.append(star)
        return ans 


# @lc code=end

asteroids = [15, 2, -5]
print(Solution().asteroidCollision(asteroids))
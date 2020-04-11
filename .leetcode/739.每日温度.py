#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (56.32%)
# Likes:    264
# Dislikes: 0
# Total Accepted:    37.8K
# Total Submissions: 63.4K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
#
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4,
# 2, 1, 1, 0, 0]。
#
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
#
#

from typing import List


# @lc code=start
class Solution:

    def dailyTemperatures_1(self, T: List[int]) -> List[int]:
        """
        双层遍历, 超时
        """
        n = len(T)
        res = [0] * n
        for i in range(n):
            for j in range(i, n):
                if T[j] > T[i]:
                    res[i] = j - i
                    break
        return res

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        栈
        """
        stack = []
        n = len(T)
        res = [0] * n
        for i in range(n - 1):
            if T[i + 1] > T[i]:
                res[i] = 1
                while stack and T[i + 1] > T[stack[-1]]:
                    ind = stack.pop()
                    res[ind] = i + 1 - ind
            else:
                stack.append(i) # 栈，保存递减序列
        return res


# @lc code=end

temperatures = [73, 74, 75, 71, 69, 70, 76, 73]
print(Solution().dailyTemperatures(temperatures))
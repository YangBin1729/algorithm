#
# @lc app=leetcode.cn id=781 lang=python3
#
# [781] 森林中的兔子
#
# https://leetcode-cn.com/problems/rabbits-in-forest/description/
#
# algorithms
# Medium (52.45%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 6.3K
# Testcase Example:  '[1,0,1,0,0]'
#
# 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。
#
# 返回森林中兔子的最少数量。
#
#
# 示例:
# 输入: answers = [1, 1, 2]
# 输出: 5
# 解释:
# 两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
# 之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
# 设回答了 "2" 的兔子为蓝色。
# 此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
# 因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。
#
# 输入: answers = [10, 10, 10]
# 输出: 11
#
# 输入: answers = []
# 输出: 0
#
#
# 说明:
#
#
# answers 的长度最大为1000。
# answers[i] 是在 [0, 999] 范围内的整数。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def numRabbits(self, answers: List[int]) -> int:
        """
        TODO：
        """
        from collections import Counter
        groups = [i + 1 for i in answers]     # 每种颜色的兔子有多少只 --> 判断有多少种颜色
        counts = Counter(groups) # 

        res = 0
        for i, num in counts.items():
            while num > i:
                res += i
                num -= i
            res += i
        return res


# @lc code=end

answers = [1, 0, 1, 0, 0]
print(Solution().numRabbits(answers))
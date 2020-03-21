#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (72.47%)
# Likes:    648
# Dislikes: 0
# Total Accepted:    59.3K
# Total Submissions: 81.7K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#
from typing import List


# @lc code=start
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. 递归
        KEY：关键点是生成括号的合法性的判断！！！
        """
        ans = []

        def _generate(s='', l=0, r=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if l < n:
                _generate(s + '(', l + 1, r)
            if r < l:
                _generate(s + ')', l, r + 1)

        _generate()
        return ans

    def generateParenthesis2(self, n: int) -> List[str]:
        """
        2. 队列：记录当前子串状态及左右括号的数量
        """
        from collections import deque

        ans = []
        queue = deque([('', 0, 0)])
        while any(queue):
            s, l, r = queue.popleft()
            if len(s) == 2 * n:
                ans.append(s)
            if l < n:
                queue.append((s + '(', l + 1, r))
            if r < l:
                queue.append((s + ')', l, r + 1))
        return ans

        # TODO：2.动态规划


# @lc code=end


def generateParenthesis(n):
    res = []

    def _generate(s, l, r):
        if len(s) == 2 * n:
            res.append(s)
            return 
        if l < n:
            _generate(s + '(', l + 1, r)
        if r < l:
            _generate(s + ')', l, r + 1)

    _generate('', 0, 0)
    return res

print(generateParenthesis(3))

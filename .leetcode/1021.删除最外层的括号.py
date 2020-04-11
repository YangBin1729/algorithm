#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#
# https://leetcode-cn.com/problems/remove-outermost-parentheses/description/
#
# algorithms
# Easy (75.40%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    22.9K
# Total Submissions: 30K
# Testcase Example:  '"(()())(())"'
#
# 有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+
# 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
#
# 如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
#
# 给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
#
# 对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。
#
#
#
# 示例 1：
#
# 输入："(()())(())"
# 输出："()()()"
# 解释：
# 输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
#
# 示例 2：
#
# 输入："(()())(())(()(()))"
# 输出："()()()()(())"
# 解释：
# 输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
#
#
# 示例 3：
#
# 输入："()()"
# 输出：""
# 解释：
# 输入字符串为 "()()"，原语化分解得到 "()" + "()"，
# 删除每个部分中的最外层括号后得到 "" + "" = ""。
#
#
#
#
# 提示：
#
#
# S.length <= 10000
# S[i] 为 "(" 或 ")"
# S 是一个有效括号字符串
#
#
#


# @lc code=start
class Solution:

    def removeOuterParentheses_1(self, S: str) -> str:
        n = len(S)
        idx = []     # 记录最外层括号的索引

        stack = []
        i = 0
        for j in range(n):
            if S[j] == ')':
                stack.pop()
                if not stack:
                    idx.append((i, j))
                    i = j + 1
            else:
                stack.append(j)
        return ''.join([S[i + 1:j] for i, j in idx])

    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        for char in S:
            if char == '(':
                stack.append(char)
                if len(stack) > 1:
                    res += '('
            else:
                stack.pop()
                if stack:
                    res +=')'
        return res


# @lc code=end

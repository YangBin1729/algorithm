#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#
# https://leetcode-cn.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (56.08%)
# Likes:    82
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 9.4K
# Testcase Example:  '"()"'
#
# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
#
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。
#
#
#
#
# 示例 1：
#
# 输入： "()"
# 输出： 1
#
#
# 示例 2：
#
# 输入： "(())"
# 输出： 2
#
#
# 示例 3：
#
# 输入： "()()"
# 输出： 2
#
#
# 示例 4：
#
# 输入： "(()(()))"
# 输出： 6
#
#
#
#
# 提示：
#
#
# S 是平衡括号字符串，且只含有 ( 和 ) 。
# 2 <= S.length <= 50
#
#
#


# @lc code=start
class Solution:

    def scoreOfParentheses(self, S: str) -> int:
        """
        TODO：代码还可优化
        """
        stack = []
        for char in S:
            if char == '(':
                stack.append(char)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack[-1] != '(':
                        score += stack.pop()
                    stack.pop()
                    stack.append(2 * score)
        return sum(stack)


# @lc code=end


S = "(()())()"
print(Solution().scoreOfParentheses(S))
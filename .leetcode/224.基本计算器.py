#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (36.00%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 23.3K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
# 字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
#
# 示例 1:
#
# 输入: "1 + 1"
# 输出: 2
#
#
# 示例 2:
#
# 输入: " 2-1 + 2 "
# 输出: 3
#
# 示例 3:
#
# 输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23
#
# 说明：
#
#
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。
#
#
#


# @lc code=start
class Solution:

    def calculate(self, s: str) -> int:
        """
        TODO: 栈
        """
        stack = []
        i = 0
        res = 0
        sign = 1
        while i < len(s):
            if s[i] == " ":
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                i += 1
            elif s[i] == ")":
                # print(stack)
                res = res * stack.pop() + stack.pop()
                i += 1
            elif s[i].isdigit():
                tmp = int(s[i])
                i += 1
                while i < len(s) and s[i].isdigit():
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                res += tmp * sign
        return res


# @lc code=end

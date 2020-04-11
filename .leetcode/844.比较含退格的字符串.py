#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#
# https://leetcode-cn.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (49.30%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 33.5K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
#
#
# 示例 1：
#
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#
#
# 示例 2：
#
# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
#
#
# 示例 3：
#
# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
#
#
# 示例 4：
#
# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
#
#
#
# 提示：
#
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S 和 T 只含有小写字母以及字符 '#'。
#
#
#
#
#


# @lc code=start
class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_S = []
        stack_T = []
        for char in S:
            if char != '#':
                stack_S.append(char)
            elif stack_S:
                    stack_S.pop()

        for char in T:
            if char != '#':
                stack_T.append(char)
            elif stack_T:
                    stack_T.pop()
        return stack_S == stack_T


# @lc code=end

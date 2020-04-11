#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (35.56%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 23.3K
# Testcase Example:  '"bcabc"'
#
# 给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
#
#
# 示例 1:
#
# 输入: "bcabc"
# 输出: "abc"
#
#
# 示例 2:
#
# 输入: "cbacdcbc"
# 输出: "acdb"
#
#
#
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
#
#


# @lc code=start
class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        # TODO
        chars = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < chars[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)

        return ''.join(stack)


# @lc code=end

s = "bcabc"
print(Solution().removeDuplicateLetters(s))

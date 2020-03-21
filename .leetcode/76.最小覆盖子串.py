#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.61%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 72.9K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
#
# 说明：
#
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
#
#


# @lc code=start
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        t = Counter(t)
        lookup = Counter()
        start = 0
        end = 0
        min_len = float("inf")

        res = ""
        while end < len(s):
            lookup[s[end]] += 1
            end += 1
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if end - start <= min_len:
                    res = s[start:end]
                    min_len = end - start
                lookup[s[start]] -= 1
                start += 1

        return res


# @lc code=end


S = "ADOBECODEBANC"
T = "ABC"
Solution().minWindow(S, T)
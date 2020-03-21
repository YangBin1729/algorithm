#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.14%)
# Likes:    3054
# Dislikes: 0
# Total Accepted:    327K
# Total Submissions: 1M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#


# @lc code=start
class Solution:

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        # 1. 动态规划：O(N^2)
        # res[i] 数组表示以 s[i] 为结尾的最长无重复子串
        if not s:
            return 0

        n = len(s)
        res = [1] * n
        ans = 0
        for i in range(1, n):
            longest_substring = s[i - res[i - 1]:i]
            if s[i] not in longest_substring:
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i - 1] - longest_substring.index(s[i])
            ans = max(ans, res[i])
        return ans

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        # 2. 集合+滑动窗口：索引 i~j 为最长子串
        if not s:
            return 0

        ans = 0
        n = len(s)
        i = j = 0

        lookup = set()
        while i < n and j < n:
            if not s[j] in lookup:
                lookup.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                lookup.remove(s[i])
                i += 1
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 3. 字典：
        # KEY：利用字典记录每个字符的最新索引
        if not s:
            return 0

        ans = 0
        end = -1
        dic = {}

        for i, c in enumerate(s):
            if c in dic and dic[c] > end:
                end = dic[c]
                dic[c] = i
            else:
                dic[c] = i
                ans = max(ans, i - end)

        return ans


# @lc code=end
s = 'pwwkew'
print(Solution().lengthOfLongestSubstring(s))
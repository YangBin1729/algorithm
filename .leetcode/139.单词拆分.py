#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (42.68%)
# Likes:    337
# Dislikes: 0
# Total Accepted:    37.5K
# Total Submissions: 86.1K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
#
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#
#
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
#
#
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#
#

from typing import List


# @lc code=start
class Solution:

    def wordBreak_1(self, s: str, wordDict: List[str]) -> bool:
        """
        1. 递归：超时
        """
        wordSet = set(wordDict)
        if not s:
            return True

        i = 0
        while i < len(s):
            if s[:i + 1] in wordSet:
                if self.wordBreak(s[i + 1:], wordDict):
                    return True
            i += 1
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        2. 动态规划
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


# @lc code=end

s = "leetcode"
wordDict = ["leet", "code"]
Solution().wordBreak(s, wordDict)
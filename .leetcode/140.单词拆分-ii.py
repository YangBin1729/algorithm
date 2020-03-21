#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (37.02%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    12K
# Total Submissions: 31.8K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
#
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#
#
# 示例 3：
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
#
#
#

from typing import List


# @lc code=start
class Solution:

    def wordBreak_1(self, s: str, wordDict: List[str]) -> List[str]:
        """
        回溯
        FIXME: 超时
        """
        ans = []
        wordSet = set(wordDict)

        def backtrack(s, res):
            if not s:
                ans.append(' '.join(res))
                return
            for i in range(len(s)):
                if s[:i + 1] in wordSet:
                    backtrack(s[i + 1:], res + [s[:i + 1]])

        backtrack(s, [])
        return ans

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        动态规划 + 回溯：
        - dp[i] 表示 s[i:] 是否可拆分
        """
        n = len(s)
        wordSet = set(wordDict)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i:j + 1] in wordSet and dp[j + 1]:
                    dp[i] = True

        ans = []

        def backtrack(s, i, res):
            if i == n:
                ans.append(' '.join(res))
                return
            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet and dp[j + 1]:     # 当剩余部分可拆分时，才进行回溯，避免不必要的分支
                    backtrack(s, j + 1, res + [s[i:j + 1]])

        backtrack(s, 0, [])
        return ans


# @lc code=end

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))


def wordBreak(s: str, wordDict: List[str]) -> List[str]:

    ans = []
    wordSet = set(wordDict)

    def backtrack(s, i, res):
        if i == len(s):
            ans.append(' '.join(res))
            return
        for j in range(i, len(s)):
            if s[i:j + 1] in wordSet:
                backtrack(s, j + 1, res + [s[i:j + 1]])

    backtrack(s, 0, [])
    return ans


# print(wordBreak(s, wordDict))

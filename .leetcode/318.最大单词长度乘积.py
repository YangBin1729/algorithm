#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (59.41%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 9.2K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j])
# 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
#
# 示例 1:
#
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16
# 解释: 这两个单词为 "abcw", "xtfn"。
#
# 示例 2:
#
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4
# 解释: 这两个单词为 "ab", "cd"。
#
# 示例 3:
#
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0
# 解释: 不存在这样的两个单词。
#
#

from typing import List

# @lc code=start
class Solution:

    def maxProduct(self, words: List[str]) -> int:
        """
        暴力法
        # TODO：加速
        """
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res


# @lc code=end

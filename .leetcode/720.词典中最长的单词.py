#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (44.03%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    6.4K
# Total Submissions: 14K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
#
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
#
# 若无答案，则返回空字符串。
#
# 示例 1:
#
#
# 输入:
# words = ["w","wo","wor","worl", "world"]
# 输出: "world"
# 解释:
# 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
#
#
# 示例 2:
#
#
# 输入:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出: "apple"
# 解释:
# "apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
#
#
# 注意:
#
#
# 所有输入的字符串都只包含小写字母。
# words数组长度范围为[1,1000]。
# words[i]的长度范围为[1,30]。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def longestWord(self, words: List[str]) -> str:
        # KEY
        import collections
        from functools import reduce
        Trie = lambda: collections.defaultdict(Trie)

        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
            # root = trie
            # for char in word:
            #     root = root[char]
            # root[END] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])
        return ans


# @lc code=end

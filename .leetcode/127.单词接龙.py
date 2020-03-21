#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (38.18%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    17.2K
# Total Submissions: 44.7K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
#
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
#
#
# 说明:
#
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
#
#
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
#
#
from typing import List


# @lc code=start
class Solution:

    def ladderLength_1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1. BFS：整个变换过程是一颗状态树
        将字典中只相差一个字母的的单词保存起来，提高查询速度
        FIXME: 超时
        """
        from collections import deque, defaultdict

        N = len(beginWord)
        queue = deque([(beginWord, 1)])
        explored = set(beginWord)

        all_combo_dict = defaultdict(list)    
        for word in wordList:
            for i in range(N):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        while queue:
            curr, changes = queue.popleft()
            for i in range(N):
                word = curr[:i] + "*" + curr[i + 1:]
                for s in all_combo_dict[word]:
                    if s == endWord:
                        return changes + 1
                    if s not in explored:
                        queue.append((s, changes + 1))
                        explored.add(s)
                        print('-->' + s)
        return 0

    def ladderLength_2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1. BFS：每次遍历字典，找到满足转换规则的单词
        FIXME: 超时
        """
        from collections import deque

        def isValid(curr, next):
            return sum([c != n for c, n in zip(curr, next)]) == 1

        queue = deque([(beginWord, 1)])
        explored = set(beginWord)

        while queue:
            curr, changes = queue.popleft()
            if curr == endWord:
                return changes
            for next in wordList:
                if isValid(curr, next) and next not in explored:
                    queue.append((next, changes + 1))
                    explored.add(next)
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        2. 双向 BFS
        - 遍历满足转换规则的单词，判断是否在词典中
        - 遍历词典，找到满足转换规则的单词
        """
        if endWord not in wordList:
            return 0
        from string import ascii_lowercase

        front, back = {beginWord}, {endWord}
        changes = 1
        wordSet = set(wordList)

        while front:
            changes += 1
            next_front = set()

            for word in front:
                for i in range(len(beginWord)):
                    for c in ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in back:
                                return changes
                            if new_word in wordSet:
                                next_front.add(new_word)
                                wordSet.remove(new_word)

                # for next in wordList:
                #     if isValid(word, next):
                #         if next in back:
                #             return changes
                #         if next in wordSet:
                #             next_front.add(next)
                #             wordSet.remove(next)
                    
            front = next_front

            if len(back) < len(front):
                front, back = back, front
        return 0


# @lc code=end

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Solution().ladderLength(beginWord, endWord, wordList)
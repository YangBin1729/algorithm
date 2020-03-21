#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (29.94%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 16K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord
# 的最短转换序列。转换需遵循如下规则：
#
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
#
#
# 说明:
#
#
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: []
#
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
#
#
from typing import List


# @lc code=start
class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # TODO:
        from collections import defaultdict
        wordSet = set(wordList)

        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)

            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])

                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_w = w[:i] + c + w[i + 1:]
                            if new_w in wordSet:
                                newlayer[new_w] += [j + [new_w] for j in layer[w]]
            wordSet -= set(newlayer.keys())
            layer = newlayer
        return res 


# @lc code=end

begin = "red"
end = "tax"
words= ["ted","tex","red","tax","tad","den","rex","pee"]
print(Solution().findLadders(begin, end, words)





































# """
# 求解全过程：
# 1. 类似 单词接龙-i 的解法
# - 队列中保存的不再是当前节点，而是到当前节点的路径列表；
# - 当访问 endWord 时，该单词即添加到 visited 集合中，所以只能求得一个解，
# """
# def findLadders1(beginWord, endWord, wordList):
#     from collections import deque
#     queue = deque([([beginWord], 1)])
#     visited = set(beginWord)

#     res = []
    
#     while queue:
#         path, changes = queue.popleft()
#         curr = path[-1]
#         if curr == endWord:
#             res.append(path)

#         for w in wordList:
#             if sum([c != n for c, n in zip(curr, w)]) == 1 and w not in visited:
#                 queue.append((path + [w], changes + 1))
#                 visited.add(w)
    
#     return res

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(findLadders1(beginWord, endWord, wordList))   

# """
# 2. 改进
# - 当访问 endWord 时，该单词不添加到 visited 集合中；
# - 得到的结果不是最短的结果
# """
# def findLadders2(beginWord, endWord, wordList):
#     from collections import deque
#     queue = deque([([beginWord], 1)])
#     visited = set(beginWord)
#     res = []
    
#     while queue:
#         path, changes = queue.popleft()
#         curr = path[-1]
#         for w in wordList:
#             if sum([c != n for c, n in zip(curr, w)]) == 1 and w not in visited:
#                 if w == endWord:
#                     res.append(path + [w])
#                     continue
#                 queue.append((path + [w], changes + 1))
#                 visited.add(w)
    
#     return res

# begin = "a"
# end = "c"
# words = ["a", "b", "c", "d"]
# print(findLadders2(begin, end, words))    

# """
# 3. 改进
# - 添加限制，当访问 endWord 时，保存一个 min_steps， 当其他路径大于该步数时，终止运行
# """
# def findLadders3(beginWord, endWord, wordList):
#     from collections import deque
#     queue = deque([([beginWord], 1)])
#     visited = set(beginWord)
#     res = []
#     min_steps = float('inf')
    
#     while queue:
#         path, changes = queue.popleft()
#         if changes >= min_steps:
#             break
#         curr = path[-1]
#         for w in wordList:
#             if sum([c != n for c, n in zip(curr, w)]) == 1 and w not in visited:
#                 if w == endWord:
#                     res.append(path + [w])
#                     min_steps = changes + 1
#                     break
#                 queue.append((path + [w], changes + 1))
#                 visited.add(w)
    
#     return res

# begin = "a"
# end = "c"
# words = ["a", "b", "c", "d"]
# print(findLadders3(begin, end, words)) 


# """
# 4. 无法获得完整解：
# - 队列为 [red,ted], [red,rex]
# - 先弹出 [red,ted], 生成新路径 [red,ted,tex], [red,ted,tad] 添加到队列
# - 此时 tex、tad 已被访问
# - 再弹出 [red,tex] 时没有后续节点了，相应的解被忽略
# # TODO：
# """
# begin = "red"
# end = "tax"
# words= ["ted","tex","red","tax","tad","den","rex","pee"]
# print(findLadders3(begin, end, words)) 
# # 输出：[["red","ted","tex","tax"],["red","ted","tad","tax"]]
# # 预期：[["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]

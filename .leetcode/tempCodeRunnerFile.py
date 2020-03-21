



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

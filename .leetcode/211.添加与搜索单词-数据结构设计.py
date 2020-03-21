#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (40.88%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 18.9K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 设计一个支持以下两种操作的数据结构：
#
# void addWord(word)
# bool search(word)
#
#
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
#
# 示例:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# 说明:
#
# 你可以假设所有单词都是由小写字母 a-z 组成的。
#
#


# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        trie = self.lookup
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        trie = self.lookup

        def _helper(word, trie):
            if '#' in trie:
                return True

            if word[0]=='.':
                for k in trie.keys():
                    if _helper(word[1:], trie[k]):
                        return True
                return False
            elif word[0] in trie:
                return _helper(word[1:], trie[word[0]])
            else:
                return False
        
        return _helper(word, trie)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '#'
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = self.end

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node
    
    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True




["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
trie = WordDictionary()
trie.addWord('a')
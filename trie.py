__author__ = 'yangbin1729'


class TrieByDict:
    """
    用嵌套词典模拟字典树的树状结构
    - 实现插入、搜索、及自动补全功能
    >>> {'bad', 'bar'}
    {'b':
         {'a':
              {'d': {'#': '#'},
               'r': {'#': '#'}}}}
    """
    
    def __init__(self):
        self.lookup = {}
        self.end_flag = '#'
    
    def insert(self, word):
        t = self.lookup
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t[self.end_flag] = self.end_flag
    
    def search(self, word):
        t = self.lookup
        for char in word:
            if char not in t:
                return False
            t = t[char]
        return self.end_flag in t
    
    def startswith(self, prefix):
        t = self.lookup
        for char in prefix:
            if char not in t:
                return False
            t = t[char]
        return True
    
    def autocomplete(self, prefix):
        t = self.lookup
        for char in prefix:
            if char not in t:
                return False
            t = t[char]
        
        res = []
        
        def _helper(pre, d):
            if "#" in d:
                res.append(pre)
                return
            for char in d:
                _helper(pre + char, d[char])
        
        _helper(prefix, t)
        return res


class Trie:
    """
    字典树每一个节点的子节点，都用一个长为 26 的数组表示，每一位代表一个字母是否存在
    """
    
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEndOfWord = False
    
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return self.TrieNode()
    
    def _charToIndex(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word):
        root = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if not root.children[index]:
                root.children[index] = self.getNode()
            root = root.children[index]
        root.isEndOfWord = True
    
    def search(self, word):
        root = self.root
        length = len(word)
        for level in range(length):
            index = self._charToIndex(word[level])
            if not root.children[index]:
                return False
            root = root.children[index]
        return root != None and root.isEndOfWord


if __name__ == '__main__':
    words = ["the", "a", "there", "anaswe", "any", "by", "their"]
    trie = Trie()
    for word in words:
        trie.insert(word)

    output = ["Not present in trie", "Present in trie"]
    print("{} ---- {}".format("the", output[trie.search("the")]))
    print("{} ---- {}".format("these", output[trie.search("these")]))
    print("{} ---- {}".format("their", output[trie.search("their")]))
    print("{} ---- {}".format("thaw", output[trie.search("thaw")]))
    
    words = {'bad', 'bed', 'bald', 'break'}
    trie = TrieByDict()
    for word in words:
        trie.insert(word)
    print(trie.autocomplete('ba'))
    

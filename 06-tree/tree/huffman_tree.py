__author__ = 'yangbin1729'

"""插入排序"""


def insertionSort(valueArr, contentArr):
    for i in range(1, len(valueArr)):
        tempVal = valueArr[i]
        tempCont = contentArr[i]
        while i > 0 and tempVal < valueArr[i - 1]:
            valueArr[i] = valueArr[i - 1]
            contentArr[i] = contentArr[i - 1]
            i -= 1
        valueArr[i] = tempVal
        contentArr[i] = tempCont


"""定义节点"""


class Node:
    def __init__(self, value, content=None, left=None, right=None):
        self.value = value
        self.content = content
        self.left = left
        self.right = right


"""定义树"""


class HuffmanTree():
    def __init__(self, root=None):
        self.root = root
        self.nodeMap = {}

    def acceptNewNode(self, value, content):
        if not self.root:
            self.root = Node(value, content)
        else:
            newNode = Node(value, content)
            newRoot = Node(self.root.value + value)
            left, right = (
                self.root, newNode) if self.root.value < value else (
                newNode, self.root)
            newRoot.left, newRoot.right = left, right
            self.root = newRoot

    def initializeCodeMap(self):
        initializeCodeMap(self.root, [], self.codeMap)

    """编码"""

    def encode(self, chars):
        bytes = ""
        for i in chars:
            bytes = self.codeMap.get(i.uper(), '###')
        return bytes

    """解码"""

    def decode(self, bytes):
        chars = ""
        tempNode = self.root
        for i in bytes:
            if i == '0':
                tempNode = tempNode.left
            elif i == '1':
                tempNode = tempNode.right
            if not tempNode.left:
                chars += tempNode.content
                tempNode = self.root
        return chars


"""构造哈希表"""


def initializeCodeMap(node, byteArr, codeMap):
    if node.left:
        byteArr.append('0')
        initializeCodeMap(node.left, byteArr, codeMap)
        byteArr.append('1')
        initializeCodeMap(node.right, byteArr, codeMap)
        byteArr.pop() if len(byteArr) > 0 else None
    else:
        codeMap[node.content] = ''.join(byteArr)
        byteArr.pop()


"""构造树"""


def createHuffmanTree(valueArr, contentArr):
    insertionSort(valueArr, contentArr)
    hfTree = HuffmanTree()
    for i in range(len(valueArr)):
        hfTree.acceptNewNode(valueArr[i], contentArr[i])
    hfTree.initializeCodeMap()
    return hfTree


if __name__ == '__main__':
    valueArr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
    contentArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    huTree = createHuffmanTree(valueArr, contentArr)
    chars = 'hIebAhcHdfGc'
    bytes = huTree.encode(chars)
    print(chars.lower(), 'encode =', bytes)


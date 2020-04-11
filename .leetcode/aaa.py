def inorder(root):
    res = []
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


def preorder(root):
    res = []
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
    return res


def postorder(root):
    res = []
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            res.append(cur.val)
            for child in cur.children:
                stack.append(child)
    return res[::-1]


def levelorder(root):
    res = []
    level = [root]
    while level:
        res.append([node.val for node in level])
        level = [child for node in level for child in [node.left, node.right] if child]
    return res



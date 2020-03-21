# 字典树
- 空间换时间
- 查询快速
- 储存了字符串间的公共前缀
每一个节点的子节点，都用一个数组表示，如长为 26 的数组，每一位代表一个字母是否存在

# 并查集


# 高级搜索

## 剪枝
**状态树**中不必要的分支：重复的、非最优的分支
- 棋类游戏

## 双向 BFS
两种朴素搜索方向：BFS、DFS，栈或队列实现；双向 BFS 从起点和终点分别做广度优先搜索，在中间相遇：
```
def BFS(graph, start, end):
    visited = set()
	front, back = [start], [end]

	while front: 
		node = front.pop() 
		visited.add(node)

		process(node) 
		nodes = generate_related_nodes(node) 
		front.push(nodes)
        
        if len(back) < len(front):
            front, back = back, front
```


## 启发式搜索
按照节点的优先级进行搜索，通过优先级队列实现:
```
def AstarSearch(graph, start, end):

	pq = PriorityQueue() 
	pq.append([start]) 
	visited.add(start)

	while pq: 
		node = pq.pop() 
		visited.add(node)

		process(node) 

        next = [node for node in generate_related_nodes(node)                if node not in visited]
        for node in next:
		    pq.push(node, priority=heuristic(node))
```
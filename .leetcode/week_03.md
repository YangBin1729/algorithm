## 分治、回溯
分治算法：
```
def divide_conquer(problem, params):
    if problem is None:
        return
    
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    subresult1 = divide_conquer(subproblem[0], params)
    subresult2 = divide_conquer(subproblem[1], params)
    ...

    resut = merge_result(subresult1, subresult2,...)
```

回溯算法框架：**其核心在于 for 循环内部的递归，在递归调用之前做选择，在递归调用之后撤销选择**
```
result = set()
def backtrack(路径, 选择列表):
    if 满足结束条件：
        result.add(路径)
        return
    for choice in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

## 深度优先搜索与广度优先搜索
普通的树或图，搜索——暴力或普通搜索，即遍历：
- 每个节点都要访问一次
- 每个节点仅仅要访问一次
- 对于节点的访问顺序不限

>> 不一定用于树结构，node.chlidren() 也并不一定是以属性的形式实现，可能通过表达式获取到下一系列节点。如二维数组，按两个索引的表达式获得下一个节点

根据访问顺序：
- 深度优先：
  - 递归形式
    ```
    visited = set()
    def dfs(node, visited):
        if node in visited:
            return
        visited.add(node)

        process(node)

        for child in node.children():
            if child not in visited:
                dfs(child, visited)
    ```
  - 非递归，通过栈实现
    ```
    def dfs(self, tree):
        if tree.root is None:
            return []

        visited, stack = [], [tree.root]

        while stack:
            node = stack.pop()
            visitied.add(node)

            process(node)

            for child in node.children():
                stack.append(child)
    ```

- 广度优先，通过队列实现
    ```
    def breadthfirst(tree):
        Q = queue(tree.root)
        while Q:
            node = Q.popleft()
            process(node)

            for child in node.children():
                Q.append(child)
    ```

- 优先级搜索/启发式搜索：推荐算法



## 贪心算法
- 每一步选择中都采取当前状态下的最好或最优的选择，从而希望导致结果是全局最优；
- 贪心算法不能回退，当下最优并不能导致最终结果全局最优；
- 贪心算法使用场景：问题能够分成子问题解决，子问题的最优解能递推到最终问题的最优解。子问题最优解成为最优子结构
- 动态规划保存最优结果，根据以前的结果对当前进行选择，有回退功能。


### 二分查找：
1. 目标函数单调性（**单调递增或递减**）：无序时只能从头到尾遍历
2. 存在上下界（bounded）：需要明确上下（或左右）指针
3. 能够通过索引访问（index accessible）：查找过程左右指针在跳跃，所以需要访问任意元素的时间复杂度皆为 O(1)
代码模板：
```
left, right = 0, len(array) - 1
while left <= right:
    mid = (left+right)/2
    if array(mid) == target:
        # find the target!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

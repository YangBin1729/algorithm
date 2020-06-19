#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (50.60%)
# Likes:    335
# Dislikes: 0
# Total Accepted:    59.4K
# Total Submissions: 117.4K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
#
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#


# @lc code=start
class MinStack:
    """"
    关键是：删除栈顶元素或入栈时，目标元素可能就是最小值，此时需要更新最小值
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.min_vals = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if self.min_vals == [] or x <= self.min_vals[-1]:
            self.min_vals.append(x)

    def pop(self) -> None:
        top = self.values.pop()
        if self.min_vals and top == self.min_vals[-1]:
            self.min_vals.pop()
        return top

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

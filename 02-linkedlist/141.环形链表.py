#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
# https://leetcode-cn.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (44.82%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    87.5K
# Total Submissions: 195K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，判断链表中是否有环。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 
# 你能用 O(1)（即，常量）内存解决此问题吗？
# 
#

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = f'{self.val}'
        tmp = self.next
        while tmp is not None:
            s += f'-->{tmp.val}'
            tmp = tmp.next
        return s + '-->NULL'



# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        1. 快慢指针
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle_2(self, head: ListNode) -> bool:
        """
        2. 利用集合记录已访问的节点，额外的 O(N) 空间消耗
        """
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

# @lc code=end


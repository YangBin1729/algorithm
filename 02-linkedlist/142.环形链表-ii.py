#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (46.37%)
# Likes:    291
# Dislikes: 0
# Total Accepted:    40K
# Total Submissions: 86.1K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 说明：不允许修改给定的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 你是否可以不用额外空间解决此题？
# 
#

# Definition for singly-linked list.
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

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        1. 快慢指针：
        入环点的位置为 r，fast、slow 两个指针在环 a 处相遇，环长度 a+b
        slow 移动长度 l1=r+a，则 fast 移动长度 l2=r+a+b+a，l2=2*l1-->r=b
        
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                start = head
                while start.next:
                    if slow==start:
                        return start 
                    start = start.next
                    slow = slow.next
        return None
                    
    def detectCycle2(self, head: ListNode) -> ListNode:
        """
        2. 集合保存访问过的节点，额外的空间 O(N)
        """
        nodeList = set()
        while head:
            if head in nodeList:
                return head
            nodeList.add(head)
            head = head.next
        return None                           

# @lc code=end


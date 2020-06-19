#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (63.21%)
# Likes:    353
# Dislikes: 0
# Total Accepted:    56.6K
# Total Submissions: 89.6K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
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

    def swapPairs_1(self, head: ListNode) -> ListNode:
        """  
        1. 递归解法
        """
        if not (head and head.next):
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next

    def swapPairs(self, head: ListNode) -> ListNode:
        """
        2. 递推解法：多个节点 prev、a1、a2、next 的交替操作；
        难点：要返回处理后链表的 首节点 --> 设置一个 dummy 节点！！
        """
        prev = dummy = ListNode(None)
        prev.next = head
        while prev.next and prev.next.next:
            a1 = prev.next
            a2 = a1.next

            a1.next = a2.next
            a2.next = a1
            prev.next = a2

            prev = a1
        return dummy.next


# @lc code=end

nodes = [ListNode(i) for i in range(1, 6)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

Solution().swapPairs(head)
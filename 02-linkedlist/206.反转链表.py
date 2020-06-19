#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (65.83%)
# Likes:    676
# Dislikes: 0
# Total Accepted:    129K
# Total Submissions: 195.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
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

    def reverseList_1(self, head: ListNode) -> ListNode:
        """
        1. 迭代：prev、head、next 三个指针的依次操作
        """
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def reverseList_2(self, head: ListNode) -> ListNode:
        """
        2. 迭代：尾插法
        """
        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head

        prev = dummy
        tail = prev
        while tail.next:
            tail = tail.next

        while prev.next != tail:
            cur = prev.next
            prev.next = cur.next
            cur.next = tail.next
            tail.next = cur
        return dummy.next

    def reverseList_3(self, head: ListNode) -> ListNode:
        """
        0->1->2->3->4
        0->2->1->3->4
        0->3->2->1->4
        0->4->3->2->1
        """
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        end = head
        prev = head
        while end.next:
            curr = end.next
            nxt = curr.next

            dummy.next = curr
            end.next = nxt
            curr.next = prev
            prev = curr

        return dummy.next

    def reverseList(self, head: ListNode) -> ListNode:
        """
        3. 递归
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# @lc code=end

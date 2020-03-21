#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (55.24%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    29.9K
# Total Submissions: 54.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
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

    def reverseKGroup_1(self, head: ListNode, k: int) -> ListNode:
        """
        KEY:  1. 尾插法
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        tail = dummy

        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break

            head = pre.next
            while pre.next != tail:
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
            pre = head
            tail = head
        return dummy.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        2. 转换成节点列表，会消耗 O(N) 的空间
        """
        if not head:
            return head

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        for i in range(0, len(nodes), k):
            if i + k <= len(nodes):
                nodes[i:i + k] = nodes[i:i + k][::-1]

        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i + 1]

        return nodes[0]

    def reverseKGroup_2(self, head: ListNode, k: int) -> ListNode:
        """
        3. 利用栈保存连续的 k 个节点，而不是保存所有节点
        """
        dummy = ListNode(None)
        dummy.next = head

        prev = dummy
        while True:
            stack = []
            count = k
            start = prev.next
            while count and start:
                count -= 1
                stack.append(start)
                start = start.next

            if count:
                break

            while stack:
                prev.next = stack.pop()
                prev = prev.next

            prev.next = start
        return dummy.next


# @lc code=end

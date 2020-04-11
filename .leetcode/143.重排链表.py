#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (53.15%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 30.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
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

    def __repr__(self):
        return self.__str__()


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def reorderList_1(self, head: ListNode) -> None:
        """
        暴力法，每次找到最终节点：超时
        """
        start = head
        prev = head
        while start and start.next and start.next.next:
            curr = start.next
            while prev.next and prev.next.next:
                prev = prev.next
            tail = prev.next

            prev.next = None
            start.next = tail
            tail.next = curr

            start = curr
            prev = start
        return head

    def reorderList(self, head: ListNode) -> None:
        """
        快慢指针找到后半部分节点，然后反转，再拼接
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        part2 = slow
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt 
            return prev
        part2 = reverse(part2)

        part1 = head
        while part2 != part1:
            nxt1 = part1.next
            part1.next = part2
            if nxt1 == part2:
                break
            nxt2 = part2.next
            part2.next = nxt1
            part1 = nxt1
            part2 = nxt2
        return head
        


# @lc code=end


vals = [1, 2, 3, 4, 5, 6]
nodes = [ListNode(val) for val in vals]
for i in range(len(vals) - 1):
    nodes[i].next = nodes[i + 1]
head = nodes[0]


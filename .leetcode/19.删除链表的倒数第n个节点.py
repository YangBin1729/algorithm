#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (36.61%)
# Likes:    698
# Dislikes: 0
# Total Accepted:    126K
# Total Submissions: 334.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeNthFromEnd_1(self, head: ListNode, n: int) -> ListNode:
        """
        1. 扫描两遍
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head

        i = 0
        prev = dummy
        while i < length - n:
            i += 1
            prev = prev.next
        prev.next = prev.next.next

        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        KEY: 2. 双指针
        """
        dummy = ListNode(0)
        dummy.next = head

        front = dummy
        back = dummy
        i = 0
        while front:
            if i < n + 1:
                front = front.next
                i += 1
            # i==n+1 时表示 front 和 back 之间相差 n+1 个节点
            # 然后 front 和 back 一起先后移动
            # 到 front 为空，back.next 即为倒数第 n 个节点
            else:
                front = front.next
                back = back.next
        back.next = back.next.next
        return dummy.next


# @lc code=end

#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (54.12%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    26.9K
# Total Submissions: 48.1K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:

        a1 = larger = ListNode(float('inf'))
        a2 = smaller = ListNode(float('-inf'))

        while head:
            if head.val >= x:
                a1.next = head
                a1 = a1.next
            else:
                a2.next = head
                a2 = a2.next
            head = head.next
        a1.next = None
        a2.next = larger.next
        return smaller.next


# @lc code=end

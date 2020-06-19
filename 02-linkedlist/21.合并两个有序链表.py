#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (58.59%)
# Likes:    755
# Dislikes: 0
# Total Accepted:    152.2K
# Total Submissions: 259.4K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
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

    def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1. 递归：
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        2. 迭代     
        KEY：定义一个辅助的前置节点指针
        """
        dummy = ListNode(None)
        
        prev = dummy
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        prev.next = l1 if l1 is not None else l2
        return dummy.next


# @lc code=end

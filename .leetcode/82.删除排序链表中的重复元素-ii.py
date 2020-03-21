#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (44.59%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 72.8K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates_1(self, head: ListNode) -> ListNode:
        """
        1. 递归
        """
        if not head or not head.next:
            return head

        if head.val != head.next.val:
            p = self.deleteDuplicates(head.next)
            head.next = p
            return head
        else:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)


    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        TODO: 2. 迭代 
        """
        if not head or not head.next:
            return head

            


# @lc code=end

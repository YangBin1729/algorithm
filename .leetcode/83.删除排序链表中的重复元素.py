#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (48.38%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    75.1K
# Total Submissions: 152.7K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        1. 递归
        """

        if not head or not head.next:
            return head

        while head.next and head.val == head.next.val:
            head = head.next
        head.next = self.deleteDuplicates(head.next)
        return head


# @lc code=end

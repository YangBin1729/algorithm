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
        TODO: 2. 迭代，快慢指针
        """
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head

        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next

    def deleteDuplicates_2(self, head: ListNode) -> ListNode:
        """
        TODO: 2. 迭代 
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        flag = False     # 表征是否出现了重复的元素
        while curr:
            while curr.next and curr.next.val == curr.val:
                flag = True
                curr = curr.next
                # 移动到相同元素的最后一位
            if flag and curr:
                # 出现了重复元素时，继续下移一位 --> 忽略了所有相同元素
                prev.next = curr.next
                flag = False
            else:
                prev.next = curr
                prev = curr
            curr = curr.next

        return dummy.next


# @lc code=end

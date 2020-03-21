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

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        1. 暴力法：找到最终结点，然后更改指针
        超时
        """
        if not head:
            return head
        
        second_last = prev = head
        while prev.next:
            while second_last.next and second_last.next.next:
                second_last = second_last.next
            if second_last == prev:
                break            
            last = second_last.next
            second_last.next = None
            
            next_ = prev.next
            last.next = next_
            prev.next = last
            second_last = prev = next_
        return head

        








# @lc code=end


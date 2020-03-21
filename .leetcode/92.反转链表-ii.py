#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (48.10%)
# Likes:    308
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 72.2K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseBetween_1(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        1. 找到并记录第 m-1 和 第 n 个节点，然后开始逆转
        """
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        i = 0
        while True:
            if i == m - 1:
                prev = cur
            if i == n:
                last = cur
                p = prev.next
                prev.next = last

                end = last.next
                next = end
                while p != end:
                    tmp = p.next
                    p.next = next
                    next = p
                    p = tmp
                break

            cur = cur.next
            i += 1
        return dummy.next

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        2. 到 m 个节点，依次将后面节点插到前面
        """
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        i = 0
        while i < m - 1:
            cur = cur.next
            i += 1
        prev = cur

        end = prev.next
        tmp = end.next
        for _ in range(n - m):
            end.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
            tmp = end.next

        return dummy.next


# @lc code=end

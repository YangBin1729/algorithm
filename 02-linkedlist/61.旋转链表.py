#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (39.48%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    44.9K
# Total Submissions: 112.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def rotateRight_1(self, head: ListNode, k: int) -> ListNode:
        """
        1. 暴力法
        超时
        """
        if not head or not head.next:
            return head

        for _ in range(k):
            tail = head
            while tail.next and tail.next.next:
                tail = tail.next
            start = tail.next
            start.next = head
            tail.next = None
            head = start
        return head

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        2. 直接寻找到旋转点
        """
        # 链表长度及最后节点
        n = 0
        last = head
        while last:
            last = last.next
            n += 1

        # 找到翻转处节点
        ind = n - k % n
        i = 1
        tail = head
        while i < ind:
            tail = tail.next
            i += 1

        last.next = head
        head = tail.next
        tail.next = None

        return head


# @lc code=end

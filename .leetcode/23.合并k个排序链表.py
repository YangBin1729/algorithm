#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (48.03%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    68.1K
# Total Submissions: 140.4K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#

from typing import List


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
            
        def merge(nodeA, nodeB):
            dummy = ListNode(None)
            prev = dummy
            while nodeA and nodeB:
                if nodeA.val < nodeB.val:
                    prev.next = nodeA
                    nodeA = nodeA.next
                else:
                    prev.next = nodeB
                    nodeB = nodeB.next
                prev = prev.next
            prev.next = nodeA if nodeA else nodeB
            return dummy.next
        
        from functools import reduce
        return reduce(merge, lists)


# @lc code=end

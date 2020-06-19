/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 *
 * https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
 *
 * algorithms
 * Medium (63.21%)
 * Likes:    353
 * Dislikes: 0
 * Total Accepted:    56.6K
 * Total Submissions: 89.6K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
 *
 * 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 *
 *
 *
 * 示例:
 *
 * 给定 1->2->3->4, 你应该返回 2->1->4->3.
 *
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
  public:
    ListNode *swapPairs(ListNode *head) {
        // 递归解法
        // if (head == nullptr or head->next == nullptr) {
        //     return head;
        // };
        // ListNode *next = head->next;
        // head->next = swapPairs(next->next);
        // next->next = head;
        // return next;

        // TODO:非递归的解法
        ListNode *prev = new ListNode(0);
        prev->next = head;
        ListNode *temp = prev;
        while (temp->next != nullptr && temp->next->next != nullptr) {
            ListNode *start = temp->next;
            ListNode *end = temp->next->next;
            temp->next = end;
            start->next = end->next;
            end->next = start;
            temp = start;
        }
        return prev->next;
    };
};
// @lc code=end

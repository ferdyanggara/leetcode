"""
Link: https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        previous_list_node_remainder = 0
        list_node_to_return = ListNode()
        list_node_to_return_original = list_node_to_return
        while True:
            list_node_sum = l1.val + l2.val + previous_list_node_remainder
            if previous_list_node_remainder == 1:
                previous_list_node_remainder = 0
            if list_node_sum >= 10:
                previous_list_node_remainder = 1
                list_node_sum -= 10
            list_node_to_return.val = list_node_sum
            if l1.next is None and l2.next is None:
                break
            if l1.next is None:
                l1.next = ListNode()
            if l2.next is None:
                l2.next = ListNode()
            l1 = l1.next
            l2 = l2.next
            list_node_to_return.next = ListNode()
            list_node_to_return = list_node_to_return.next
        if previous_list_node_remainder != 0:
            list_node_to_return.next = ListNode(1)
        return list_node_to_return_original

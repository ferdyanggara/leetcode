"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        node_list = []
        while node.next is not None:
            node_list.append(node)
            node = node.next
        node_list.append(node)
        if len(node_list) == 1:
            return None
        if n == 1:
            node_list[-2].next = None
        elif n == len(node_list):
            head = node_list[0].next
        else:
            node_list[-n - 1].next = node_list[-n + 1]
        return head

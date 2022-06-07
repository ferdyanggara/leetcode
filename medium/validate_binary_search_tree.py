"""
Link: https://leetcode.com/problems/validate-binary-search-tree/
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        to_visit = [(root, -2e31, 2e31-1)]
        while len(to_visit) > 0:
            root, min_val, max_val = to_visit.pop(0)
            root_val = root.val
            if root.left is not None:
                if root.left.val < root_val and root.left.val > min_val:
                    to_visit.append((root.left, min_val, root_val))
                else:
                    return False
            if root.right is not None:
                if root.right.val > root_val and root.right.val < max_val:
                    to_visit.append((root.right, root_val, max_val))
                else:
                    return False
        return True

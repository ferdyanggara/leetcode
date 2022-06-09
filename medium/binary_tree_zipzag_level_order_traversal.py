"""
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        result = []
        level = 0
        
        while q:
            currentnode = deque()
            levelsize = len(q)
            for _ in range(levelsize):
                node = q.popleft()
                if level % 2 == 0:
                    currentnode.append(node.val)
                else:
                    currentnode.appendleft(node.val)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(currentnode)
            level += 1
        return result 

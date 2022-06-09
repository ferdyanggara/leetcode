# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (root.left is None) ^ (root.right is None):
            return False
        
        to_visit = [root.left, root.right]
        while len(to_visit) > 0:
            left = to_visit.pop(0)
            right = to_visit.pop(0)
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                to_visit.append(left.left)
                to_visit.append(right.right)
                to_visit.append(left.right)
                to_visit.append(right.left)
            else:
                return False
        return True

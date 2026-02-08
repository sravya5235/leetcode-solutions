# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            # Base case: empty tree has height 0
            if not node:
                return 0
            
            # Recursively get heights of left and right subtrees
            left = helper(node.left)
            right = helper(node.right)
            
            # If either subtree is unbalanced, propagate -1
            if left == -1 or right == -1:
                return -1
            
            # If height difference > 1, current tree is unbalanced
            if abs(left - right) > 1:
                return -1
            
            # Return height of current tree
            return max(left, right) + 1
        
        return helper(root) != -1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        values = []

        # Step 1: Inorder traversal to collect sorted values
        self.inorder(root, values)

        # Step 2: Build balanced BST from sorted values
        return self.buildBalanced(values, 0, len(values) - 1)

    def inorder(self, node, values):
        if not node:
            return

        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)

    def buildBalanced(self, values, start, end):
        if start > end:
            return None

        mid = start + (end - start) // 2
        root = TreeNode(values[mid])

        root.left = self.buildBalanced(values, start, mid - 1)
        root.right = self.buildBalanced(values, mid + 1, end)

        return root
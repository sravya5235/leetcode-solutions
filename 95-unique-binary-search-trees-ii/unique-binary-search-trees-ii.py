class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        from functools import lru_cache

        @lru_cache(None)
        def build(l, r):
            if l > r:
                return [None]

            res = []

            for root in range(l, r + 1):
                leftTrees = build(l, root - 1)
                rightTrees = build(root + 1, r)

                for lt in leftTrees:
                    for rt in rightTrees:
                        node = TreeNode(root)
                        node.left = lt
                        node.right = rt
                        res.append(node)

            return res

        return build(1, n)

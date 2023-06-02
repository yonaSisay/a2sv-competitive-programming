class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)

        def dp(node, used):
            if (node, used) in memo:
                return memo[(node, used)]
            if not node:
                return 0
            use = 0
            notuse = 0

            if not used:
                use = dp(node.left,True) + dp(node.right,True) + node.val
            notuse = dp(node.left, False) + dp(node.right, False)
            
            memo[(node,used)] = max(use, notuse)

            return  memo[(node,used)]
        
        return dp(root, False)
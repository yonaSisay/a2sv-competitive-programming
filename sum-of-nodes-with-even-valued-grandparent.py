# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        summ = 0

        def dfs(node):
            nonlocal summ
            
            if not node:
                return
            if not node.val % 2:
                if node.left and node.left.left:
                    summ += node.left.left.val
                if node.left and node.left.right:
                    summ += node.left.right.val
                if node.right and node.right.left:
                    summ += node.right.left.val
                if node.right and node.right.right:
                    summ += node.right.right.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return summ
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        summ = 0

        def dfs(node, parent = None, grand = None):
            nonlocal summ
            if not node:
                return
            
            if grand != None and not grand.val % 2 :
                summ += node.val
            
            dfs(node.left , node, parent)
            dfs(node.right , node, parent)
            
        dfs(root)

        return summ
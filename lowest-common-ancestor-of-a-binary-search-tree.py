# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowest(node):
            if not node: return
            if p.val <= node.val <= q.val: return node
            if p.val >= node.val >= q.val: return node

            if p.val > node.val:
                return lowest(node.right)
            else:
                return lowest(node.left)
            return node
        
        return lowest(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def recur(node, val):
            if not node:
                return TreeNode(val)
            
            if val >= node.val:
                node.right = recur(node.right, val)
            elif val < node.val:
                node.left = recur(node.left, val)

            return node
        
        root = None

        for num in preorder:
            root  = recur(root, num)

        return root
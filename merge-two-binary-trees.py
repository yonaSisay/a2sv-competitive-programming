# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1 , root2):
            if not root1 and not root2:
                return 
            if not root2:
                return root1
            if not root1:
                return root2
            
            root2.val = root1.val + root2.val

            l = merge(root1.left, root2.left)
            r = merge(root1.right, root2.right)

            root2.left = l
            root2.right = r

            return root2
    
        return merge(root1, root2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def traverse(self,left, right):
        if not left and not right : return True
        
        if not left: return False
        if not right: return False
        
        if left.val != right.val:
            return False

        l = self.traverse(left.left, right.right)
        r = self.traverse(left.right, right.left)

        return l and r
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root,root)
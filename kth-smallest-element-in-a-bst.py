# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:        
        def small(node):
            nonlocal k
            if not node: return None
            left = small(node.left)         
            
            if left != None: return left
            
            k -= 1
            
            if k == 0 : return node.val

            right = small(node.right)

            if right != None : return right

        return small(root)
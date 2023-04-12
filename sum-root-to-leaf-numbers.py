# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def recur(node, arr):
            nonlocal summ
            if not node:
                return
            
            arr.append(node.val)

            if  node.left == None and  node.right == None:
                v = ''.join(list(map(str,arr)))
                summ += int(v)
                return
            

            recur(node.left, arr[:])
            recur(node.right, arr[:])
        recur(root,[])
        
        return summ
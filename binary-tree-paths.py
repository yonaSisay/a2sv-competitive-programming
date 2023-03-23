# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def traverse(self,root, arr):
        if not root:
            return

        if not root.left and not root.right:
            self.ans.append('->'.join(map(str,arr + [root.val])))
        
        self.traverse(root.left, arr + [root.val])
        self.traverse(root.right, arr + [root.val])

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.traverse(root,[])
        
        return self.ans
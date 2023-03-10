# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mapp = defaultdict(list)
        root.val = 1
        def func(node , level):  
            if not node:
                return 
            if node.left:
                node.left.val = node.val * 2
            if node.right:
                node.right.val = node.val * 2 + 1
            
            mapp[level].append(node.val)

            func(node.left, level + 1)
            func(node.right, level + 1)
        func(root, 0)      

        maxx = float(-inf)

        for key in mapp:
            value = mapp[key]
            temp = value[-1] - value[0] + 1
            
            maxx = max(temp, maxx)
        
        return maxx
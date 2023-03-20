# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapp = defaultdict(list)

        def recur(node, row , col):
            if not node: return

            mapp[col].append([row,node.val])

            recur(node.left, row + 1,col - 1)
            recur(node.right, row + 1, col + 1)

        recur(root,0, 0)
        final = []
        keys = list(sorted(mapp.keys()))
        
        
        for key in keys:
            nums = sorted(mapp[key])
            val = []
            for num in nums:
                val.append(num[1])
            final.append(val)
                    
        return final
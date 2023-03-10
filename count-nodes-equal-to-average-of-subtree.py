# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def ave(node, ans):
            
            if not node:
                return 0,0,ans
            
            lsum,left,ans = ave(node.left,ans)
            rsum,right,ans = ave(node.right, ans)

            summ = lsum + rsum + node.val
            nodes = left + right + 1
            aave = summ // nodes

            if aave == node.val:
                ans[0] += 1
            
            return summ , nodes, ans

        return ave(root, [0])[2][0]
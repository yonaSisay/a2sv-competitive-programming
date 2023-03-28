# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        mapp = defaultdict(int)
        count = 0
        mapp[0] = 1

        def recur(prefixSum,node):
            nonlocal count, mapp
            

            if not node:
                return
            
            prefixSum += node.val

            if (prefixSum - targetSum) in mapp:
                count += mapp[prefixSum - targetSum]
            
            mapp[prefixSum] += 1

            recur(prefixSum, node.left)
            recur(prefixSum, node.right)

            mapp[prefixSum] -= 1
        
        recur(0, root)

        return count
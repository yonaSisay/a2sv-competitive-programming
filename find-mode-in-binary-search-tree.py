# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mapp = defaultdict(int)

        def recur(node):
            if not node: return
            
            mapp[node.val] += 1

            recur(node.left)
            recur(node.right)

        recur(root)
        ans = []
        a = max(mapp.values())
        for key in mapp:
            if mapp[key] == a:
                ans.append(key)        
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        mapp = defaultdict(list)

        def recur(node, k):
            if not node: return

            mapp[k].append(node.val)

            recur(node.left, k + 1)
            recur(node.right, k + 1)
        recur(root,0)

        return [mapp[k] for k in sorted(mapp)]
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxx = 0

        def recur(node, depth):
            nonlocal maxx
            if not node:
                return
            if not node.children:
                maxx = max(maxx, depth + 1)
                return
            
            for child in node.children:
                ndepth = depth + 1
                recur(child,ndepth)
        
        recur(root, 0)

        return maxx
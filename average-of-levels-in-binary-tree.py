# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            summ = 0
            count = 0

            length = len(queue)

            for i in range(length):
                node = queue.popleft()
                summ += node.val
                count += 1

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            if count:
                ans.append(summ / count)
        
        return ans
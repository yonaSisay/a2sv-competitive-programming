# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(root):
            if not root:
                return
            
            if root.left :
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)

            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        
        q = deque([target.val])
        visited = set([target.val])
        ans = []
        level = 0

        while q:

            for _ in range(len(q)):
                node = q.popleft()

                print(node, level)
                if level == k:
                    ans.append(node)

                for elm in graph[node]:
                    if elm not in visited:
                        q.append(elm)
                        visited.add(elm)
            level += 1

        return ans
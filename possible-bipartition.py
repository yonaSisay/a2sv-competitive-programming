class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()
        color = [-1]*n
        
        for elm in dislikes:
            adj[elm[0]].append(elm[1])
            adj[elm[1]].append(elm[0])
        
        def dfs(node):
            if node in visited:
                return True

            visited.add(node)

            flag = True

            for elm in adj[node]:
                if color[elm - 1] == -1:
                    color[elm - 1] = int(not color[node - 1])
                
                if color[elm - 1] == color[node - 1]:
                    return False
                flag = flag and dfs(elm)
                
            return flag

        for i in range(1, n + 1):
            if i not in visited:
                color[i - 1] = 1
                
                if not dfs(i):
                    return False
      
        return True
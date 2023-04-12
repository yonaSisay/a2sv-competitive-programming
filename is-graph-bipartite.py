class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        visited = set()
        flag = True

        def dfs(node):
            nonlocal flag
            if node in visited:
                return

            visited.add(node)        
            print(color)    
            for elm in graph[node]:
                if color[elm] == -1:
                    color[elm] = int(not color[node])
                    
                if color[elm] == color[node]:
                    flag = False
                    return

                dfs(elm)
                

        for i in range(len(graph)):  
            if i not in visited:           
                color[i] = 1
                dfs(i)
                
        return flag
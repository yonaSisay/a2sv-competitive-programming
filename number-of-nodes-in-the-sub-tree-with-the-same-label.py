class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ans = [0]*n
        visited = set()
        def dfs(node):
            visited.add(node)
            if not graph[node]:
                alpha = [0]*26
                alpha[ord(labels[node]) - ord("a")] += 1 
                ans[node] += 1
                return alpha
            alpha = [0]*26

            for elm in graph[node]:
                if elm not in visited:
                    for i,val in enumerate(dfs(elm)):
                        alpha[i] += val
       
            alpha[ord(labels[node]) - ord("a")] += 1 
            ans[node] = alpha[ord(labels[node]) - ord("a")]

            return alpha
        
        dfs(0)

        return ans
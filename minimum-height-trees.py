class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg  = defaultdict(int)
        ans = [0]*n

        for src,end in edges:
            graph[src].append(end)
            graph[end].append(src)
            indeg[src], indeg[end] = indeg[src] + 1, indeg[end] + 1
    
        que = deque()
        visited = set()

        for num in range(n):
            if indeg[num] == 1:
                que.append(num)
                visited.add(num)
        
        while que:
            node = que.popleft()

            for elm in graph[node]:
                if elm not in visited:
                    if ans[node] + 1 > ans[elm]:
                        ans[elm] = ans[node] + 1 
                    
                    indeg[elm] -= 1
                    
                    if indeg[elm] == 1:
                        que.append(elm)
                        visited.add(elm)
        maxx = max(ans)

        return [x for x in range(n) if ans[x] == maxx]
class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = defaultdict(int)

        for x,y in pairs:
            graph[x].append(y)
            graph[y].append(x)
            indeg[x] += 1
            indeg[y] += 1
        
        que = deque()
        visited = set()
        ans = []

        for key in indeg:
            if indeg[key] == 1:
                que.append(key)
                visited.add(key)
        
        while que:
            node = que.pop()
            ans.append(node)

            for elm in graph[node]:
                if elm not in visited:
                    que.append(elm)
                    visited.add(elm)

        return ans
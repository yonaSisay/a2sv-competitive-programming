class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjList = defaultdict(list)
        maxx = 0

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                p = bombs[i][:-1]
                q = bombs[j][:-1]

                dist = math.dist(p,q)
                radius = bombs[i][2]
                if i != j and dist <= radius:
                    adjList[i].append(j)
        
        def dfs(visited, idx):
            nonlocal maxx
            visited.add(idx)
            maxx = max(maxx, len(visited))
            
            for num in adjList[idx]:
                if num not in visited:
                    dfs(visited, num)

        for num in range(len(bombs)):
            dfs(set(),num)            

        return maxx
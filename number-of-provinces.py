class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = defaultdict(list)
        rowlen = len(isConnected)
        collen = len(isConnected[0])
        visited = set()
        count = 0

        for i in range(rowlen):
            for j in range(collen):
                if isConnected[i][j]:
                    adjList[i + 1].append(j + 1)
        
        def dfs(num):
            if num in visited:
                return 
            visited.add(num)
            for num in adjList[num]:
                dfs(num)
        
        for num in adjList:
            if num not in visited:
                count += 1
                dfs(num)
        
        return count
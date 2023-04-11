class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])
        visited = set()
        maxArea = 0

        arr = [[0,1],[1,0],[-1,0],[0,-1]]

        def inbound(row,col):
            return 0 <= row < rowlen and 0 <= col < collen
        area = 0
        def dfs(row, col):
            nonlocal area
            if not inbound(row,col) or (row,col) in visited or not grid[row][col]:
                return
            
            visited.add((row,col))
            area += 1
            for idx in arr:
                nr = row + idx[0]
                nc = col + idx[1]
                dfs(nr, nc, )

        for i in range(rowlen):
            for j in range(collen):
                if (i,j) not in visited and grid[i][j]:   
                    dfs(i, j)
                    maxArea = max(area, maxArea)
                    area = 0
        
        return maxArea
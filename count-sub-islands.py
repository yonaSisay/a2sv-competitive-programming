class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        vertice = [[1,0],[0,1],[-1,0],[0,-1]]
        row = len(grid1)
        col = len(grid1[0])

        def check(x, y):
            return 0 <= x < row and  0 <= y < col
        
        visited = set()
        count = 0
        flag = True

        def dfs(row, col):
            nonlocal flag
            if not grid1[row][col]:
                flag = False

            visited.add((row,col))

            for x,y in vertice:
                nr = row + x
                nc = col + y

                if check(nr,nc) and (nr,nc) not in visited and grid2[nr][nc]:
                    dfs(nr, nc)
            

        for i in range(row):
            for j in range(col):
                if (i , j) not in visited  and grid2[i][j]:
                    dfs(i,j)
                    if flag:
                        count += 1
                    flag = True
        return count
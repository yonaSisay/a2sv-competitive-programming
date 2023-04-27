class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]
        row = len(grid)
        col = len(grid[0])

        inbound = lambda x,y: 0 <= x < row and 0 <= y < col

        queue = deque()
        path = []
        queue.append((0,0))
        path.append((0,0))
        level = 0
        
        if grid[0][0]:
            return -1
        grid[0][0] = 1


        while queue:
            level += 1
            N  = len(queue) 

            for _ in range(N):
                r,c = queue.popleft()

                for x,y in directions:
                    nr , nc = r + x, c + y

                    if (nr,nc) == (row,row):
                        return level
                    if inbound(nr,nc) and not grid[nr][nc]:
                        path.append((nr,nc))
                        queue.append((nr,nc))
                        grid[nr][nc] = 1
        return -1
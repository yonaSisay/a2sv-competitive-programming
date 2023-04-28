class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        inbound = lambda x,y : 0 <= x < row and 0 <= y < col
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
       
        ans = [[0 for _ in range(col)] for _ in range(row)]
        visited = set()
        queue = deque()
        level = 0

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    queue.append([i,j])

        while queue:
            N = len(queue)
            level += 1

            for _ in range(N):
                x,y = queue.popleft()

                for r,c in directions:
                    nr, nc = r + x, c + y

                    if inbound(nr,nc) and (nr,nc) not in visited:
                        ans[nr][nc] = level
                        queue.append([nr,nc])
                        visited.add((nr,nc))
        return ans
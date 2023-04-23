class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        inbound = lambda x,y: 0  <= x < row and 0 <= y < col

        vertice = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        tobe = []
        flag = True

        def dfs(row, col):
            nonlocal flag
            visited.add((row, col))

            for x,y in vertice:
                nr,nc = x + row, y + col

                if inbound(nr,nc):
                    if board[nr][nc] == "O" and (nr,nc) not in visited:
                        tobe.append([nr,nc])
                        dfs(nr,nc)
                else:
                    flag = False
        
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and board[i][j] == "O":
                    tobe.append([i, j])
                    dfs(i,j)

                    if flag:
                        for x,y in tobe:
                            board[x][y] = "X"  
                    flag = True
                    tobe = []
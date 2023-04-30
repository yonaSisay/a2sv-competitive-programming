class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            colmap = set()
            rowmap = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in rowmap:
                        return False
                    rowmap.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in colmap:
                        return False
                    colmap.add(board[j][i])

        for x in range(0, n, 3):
            for y in range(0, n, 3):
                check = set()
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] != ".":
                            if board[i][j] in check:
                                return False
                            check.add(board[i][j])

        return True
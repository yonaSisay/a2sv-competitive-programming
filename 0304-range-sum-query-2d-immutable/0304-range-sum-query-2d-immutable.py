class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = matrix
        n, m = len(matrix),len(matrix[0])
        

        
        for i in range(n):
            temp = []
            for j in range(m):
                self.prefix[i][j] = (self.getElement(i - 1, j) + self.getElement(i , j -1) - self.getElement(i - 1, j -1) + matrix[i][j])
        
    def getElement(self , i, j):
        n, m = len(self.matrix),len(self.matrix[0])
        
        if i >= n or i < 0 or j >= m or j < 0:
            return 0
        return self.prefix[i][j] 
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = self.getElement(row2 , col2) - self.getElement(row2, col1 - 1) - self.getElement(row1 - 1, col2) + self.getElement(row1 - 1 , col1 - 1)
        
        return summ

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = 0
        for i in range(len(matrix[0])):           
            for j in range(len(matrix)-1):
                if matrix[j][0] <= target < matrix[j+1][0]:
                    index = j
                elif target >= matrix[j+1][0]:
                    index = j+1
                
        for i in range(len(matrix[index])):
            if matrix[index][i] == target:
                return True
        return False
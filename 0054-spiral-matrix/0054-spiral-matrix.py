class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        right = len(matrix[0])
        left = 0
        ans = []
        count = 0
        if len(matrix[0]) == 1:
            return [i[0] for i in matrix]
            
        while count < len(matrix) * len(matrix[0]):
            for i in range(left,right):
                ans.append(matrix[top][i])
                count += 1
            top += 1
            for i in range(top,bottom-1):
                ans.append(matrix[i][right-1])
                count += 1
            if top == bottom:
                break
            right -= 1
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom-1][i])
                count += 1
            bottom -= 1
            if right == left:
                break
                
            for i in range(bottom-1,top-1,-1):
                ans.append(matrix[i][left])
                count += 1
            left += 1
            
        return ans
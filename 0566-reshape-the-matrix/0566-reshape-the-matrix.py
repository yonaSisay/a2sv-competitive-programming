class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        arr = []
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr.append(mat[i][j])
        count = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(arr[count])
                count += 1
            ans.append(temp)
        return ans
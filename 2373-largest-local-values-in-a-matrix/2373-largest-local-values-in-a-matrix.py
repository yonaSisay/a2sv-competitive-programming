class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row-2):
            temp = []
            for j in range(col-2): 
                maxi = 0
                for k in range(i,i+3):
                    for z in range(j,j+3):
                        maxi = max(maxi,grid[k][z])
                temp.append(maxi)
            ans.append(temp)
            
        # count = 0
        # for i in range(row-2):
        #     temp = []
        #     for j in range(col-2):
        #         temp.append(arr[count])
        #         count += 1
        #     ans.append(temp)
        return ans
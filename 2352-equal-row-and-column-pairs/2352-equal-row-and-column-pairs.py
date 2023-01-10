class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        trans = []
        count = 0
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            trans.append(temp)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i]==trans[j]:
                    count +=1
        return count
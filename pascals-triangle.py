class Solution:
    def __init__(self):
        self.oldArr = [[1]]
        self.count = 0
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return self.oldArr

        newArr = []
        newArr.append(1)

        if self.oldArr:
            for i in range(len(self.oldArr[-1]) - 1):
                temp = self.oldArr[-1][i] + self.oldArr[-1][i + 1]
                newArr.append(temp)
        newArr.append(1)
        self.oldArr.append(newArr)

        return self.generate(numRows - 1)
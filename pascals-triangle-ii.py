class Solution:
    def __init__(self):
        self.lastRow = [1]

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return self.lastRow

        newArr = [1]
        n =  len(self.lastRow)
        for i in range(n - 1):
            temp = self.lastRow[i] + self.lastRow[i + 1]
            newArr.append(temp)
        newArr.append(1)
        
        self.lastRow = newArr

        return self.getRow(rowIndex - 1)
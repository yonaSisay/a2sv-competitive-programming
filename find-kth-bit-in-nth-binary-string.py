class Solution:
    def invertReverse(self, i):
        if i == 1:
            return "0"
        
        
        temp = self.invertReverse(i - 1)
        
        temp2 = ""

        for i in range(len(temp)):
            if temp[i] == "0": 
                temp2 += "1"
            else:
                temp2 += "0"

        
        temp += "1" + temp2[::-1]

        return temp
        

    def findKthBit(self, n: int, k: int) -> str:    
        return self.invertReverse(n)[k - 1]
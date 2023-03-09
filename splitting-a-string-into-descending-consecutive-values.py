class Solution:
    def splitString(self, s: str, lastVal: int = None) -> bool:
        if lastVal and lastVal == int(s) + 1:
           return True
        
        for i in range(1, len(s)):
            curr = int(s[:i])
            
            if lastVal == None or curr == lastVal - 1:
                if self.splitString(s[i:] , curr):
                    return True
        return False
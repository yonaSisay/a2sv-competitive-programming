class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = (n & 1)
        n >>= 1
        ans = True

        while n:
            if prev == (n & 1):
                ans = False
                break
            prev = (n & 1)
            n >>= 1
        
        return ans
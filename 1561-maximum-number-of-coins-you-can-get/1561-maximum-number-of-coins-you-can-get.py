class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        index = n//3
        ans = 0
        
        for i in range(index,n,2):
            ans += piles[i]
        
        return ans
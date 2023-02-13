class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return math.ceil(high/2) - math.ceil((low-1)/2)
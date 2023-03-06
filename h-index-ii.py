class Solution:
    def hIndex(self, citations: List[int]) -> int:
        high = len(citations)
        low = 0
        ans = -1
        
        while low  < high:
            mid = low + (high - low) // 2

            if citations[mid] >= len(citations) - mid:
                ans = mid
                high = mid     
            else:
                low = mid + 1     
                   
        return len(citations) - ans if ans != -1 else 0
class Solution:
    def checker (self, weights, days, mid):
        day = 1
        num= 0
        for weight in weights:
            num += weight
            if num > mid:
                day += 1
                num = weight
            
        return day <= days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            mid = (low + high ) // 2
            if self.checker(weights, days, mid):              
                high = mid
            else:               
                low = mid + 1

        return low
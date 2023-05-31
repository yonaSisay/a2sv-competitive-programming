class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) - 1
        memo = {}
        
        def recur(idx):
            nonlocal n
            if idx > n:
                return 0
            if idx in memo:
                return memo[idx]

            onestep = recur(idx + 1)
            twostep = recur(idx + 2)

            memo[idx] = min(onestep, twostep) + cost[idx]
            
            return memo[idx]
        return min(recur(0),recur(1))
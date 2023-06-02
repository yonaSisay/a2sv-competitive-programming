class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)

        def dp(idx,buyed):
            if idx >= len(prices):
                return 0
            if (idx, buyed) in memo:
                return memo[(idx,buyed)]
                
            profit = 0

            if buyed:
                use = dp(idx + 1, False) + prices[idx] - fee
                notuse = dp(idx + 1, buyed)
                profit = max(use, notuse)

            elif not buyed:
                use = dp(idx + 1, True) - prices[idx]
                notuse = dp(idx + 1, buyed)
                profit = max(use, notuse)
            
            memo[(idx, buyed)] = profit

            return profit
        return dp(0,False)
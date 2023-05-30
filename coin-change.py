class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
    
        def dp(num):
            if num < 0:
                return float('inf')
            if num == 0:
                return 0
            
            no = float('inf')

            for coin in coins:
                temp = num - coin

                if temp in memo:
                    no = min(memo[temp], no)
                    continue
                no = min(dp(temp),no)
            
            memo[num] = no + 1
            return memo[num]
        
        return dp(amount) if dp(amount) != float('inf') else -1
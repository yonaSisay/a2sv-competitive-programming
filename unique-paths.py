class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)

        inbound = lambda x,y: 0 <= x < m and 0 <= y < n
        direc = [(1,0),(0,1)]

        def dp(r,c):
            if (r,c) == (m - 1, n - 1):
                return 1
            
            if (r,c) in memo:
                return memo[(r,c)]

            summ = 0

            for x,y in direc:
                nr = r + x
                nc = c + y

                if inbound(nr,nc):
                    summ += dp(nr,nc)
                    
            memo[(r,c)] = summ
            return summ 
        
        return dp(0,0)
class Solution:
    def minSteps(self, n: int) -> int:
        A = 1
        ope = 0
        copy = 1

        while A < n:
            if n % A == 0:
                copy = A
                ope += 1
            
            A += copy
            ope += 1
        
        return ope
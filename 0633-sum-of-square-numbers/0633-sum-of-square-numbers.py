class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(sqrt(c))
        l = 0
        if sqrt(c)==r:
            return True
        while l < r:
            temp = r*r + l*l 
            if temp > c:
                r -= 1
            elif temp < c:
                l += 1
            elif temp == c:
                return True
            if (r*r)*2 == c or (l*l)*2 == c :
                return True
            
        return False
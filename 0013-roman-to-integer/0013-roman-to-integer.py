class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum = 0
        for i in range(len(s)):
            sum+=roman[s[i]]
        if "IV" in s:
            sum -= 2
        if "IX" in s:
            sum -= 2
        if "XL" in s:
            sum -= 20
        if "XC" in s:
            sum -= 20
        if "CD" in s:
            sum -= 200
        if "CM" in s:
            sum -= 200
            
        return sum
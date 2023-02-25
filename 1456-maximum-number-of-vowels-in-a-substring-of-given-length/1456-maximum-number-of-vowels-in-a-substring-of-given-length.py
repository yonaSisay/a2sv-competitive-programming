class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a':1 , 'e': 1 , 'i':0, 'o':1 , 'u':1}
        ans = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
                
        ans = max(count, ans)
        
        for i in range(k,len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            ans = max(count, ans)
        return ans
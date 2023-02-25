class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = count = 0
        for i, c in enumerate(s):
            if c in vowels:
                count += 1
            if i >= k and s[i - k] in vowels:
                count -= 1
            ans  = max(count, ans)
        return ans
        
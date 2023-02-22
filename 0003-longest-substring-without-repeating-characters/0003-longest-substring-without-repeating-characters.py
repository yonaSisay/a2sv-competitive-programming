class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxx = 0
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                maxx = max(len(window),maxx)
                r += 1
            elif s[r] in window:
                window.remove(s[l])
                l += 1
        return maxx
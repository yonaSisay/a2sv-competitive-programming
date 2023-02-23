class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = Counter()
        l = 0
        maxx = 0
        
        for i in range(len(s)):
            seen[s[i]] += 1
            while seen.total() > max(seen.values()) + k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            maxx = max(seen.total(), maxx)
        
        return maxx
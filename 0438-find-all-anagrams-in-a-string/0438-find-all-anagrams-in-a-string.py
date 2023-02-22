class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = defaultdict(int)
        target = defaultdict(int)
        ans = []
        
        if len(s) < len(p):
            return ans
        
        for char in p:
            target[char] += 1
        for i in range(len(p)):
            window[s[i]] += 1
        index = 0
                
        for i in range(len(s)-len(p)):
            if window == target:
                ans.append(i)
            window[s[i]] -= 1
            window [s[i+len(p)]] += 1
            if window[s[i]] == 0:
                del window[s[i]]
            index = i + 1
        if target == window:
            ans.append(index)
        return ans
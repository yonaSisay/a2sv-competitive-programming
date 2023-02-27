class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = 0
        target = Counter(t)
        mapp = defaultdict(int)
        ans = []
        l = 0
        for char in t:
            mapp[char] = 0
        
        for i in range(len(s)):
            if s[i] in target:
                if mapp[s[i]] < target[s[i]]:
                    count += 1
                mapp[s[i]] += 1
            
            while count >= len(t):
                ans.append([i-l,l,i])
                if s[l] in target: 
                    mapp[s[l]] -= 1
                    if mapp[s[l]] < target[s[l]]:
                        count -= 1
                l += 1
        ans.sort()        
        if len(ans) > 0:
            return s[ans[0][1]:ans[0][2] + 1]
        return ""
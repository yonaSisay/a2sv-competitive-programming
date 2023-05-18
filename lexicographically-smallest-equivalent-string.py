class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = defaultdict(str)
        ans = []
        for i in range(len(s1)):
            rep[s1[i]] = s1[i]
            rep[s2[i]] = s2[i]
        
        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            repx = find(x)
            repy = find(y)

            if repx != repy:
                if ord(repx) < ord(repy):
                    rep[repy] = repx
                else:
                    rep[repx] = repy

        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        for ch in baseStr:
            if ch in rep:
                ans.append(find(ch))
            else:
                ans.append(ch)
        
        return "".join(ans)
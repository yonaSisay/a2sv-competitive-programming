class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = defaultdict(str)
        ans = []
        size = defaultdict(int)

        def find(x):
            if x not in rep:
                rep[x] = x
                size[x] = 1
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x,y):
            parx  = find(x)
            pary = find(y)

            if parx != pary:
                if size[parx] < size[pary]:
                    rep[parx] = pary
                    size[pary] += size[parx]
                else:
                    rep[pary] = parx
                    size[parx] += size[pary]

        for charr in equations:
            x , no, eq, y = list(charr)

            if no == "=":
                union(x,y)
            else:
                ans.append((x,y))
            
        for x,y in ans:
            if find(x) == find(y):
                return False
        return True